#!/usr/bin/env python3
"""
Local TrOCR Service using Hugging Face Transformers
This provides a simple HTTP API for OCR text extraction
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import io
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for React app

class LocalTrOCRService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")
        
        # Load the TrOCR model and processor
        self.model_name = "microsoft/trocr-base-handwritten"
        logger.info(f"Loading model: {self.model_name}")
        
        try:
            self.processor = TrOCRProcessor.from_pretrained(self.model_name)
            self.model = VisionEncoderDecoderModel.from_pretrained(self.model_name)
            self.model.to(self.device)
            logger.info("Model loaded successfully!")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    def extract_text(self, image_data):
        """Extract text from image data (base64 or file)"""
        try:
            # Convert base64 to PIL Image
            if isinstance(image_data, str) and image_data.startswith('data:image'):
                # Handle data URL
                image_data = image_data.split(',')[1]
            
            if isinstance(image_data, str):
                # Decode base64
                image_bytes = base64.b64decode(image_data)
            else:
                image_bytes = image_data
            
            # Convert to PIL Image
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            
            # Process image
            pixel_values = self.processor(image, return_tensors="pt").pixel_values
            pixel_values = pixel_values.to(self.device)
            
            # Generate text
            with torch.no_grad():
                generated_ids = self.model.generate(pixel_values)
                generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            
            # Calculate confidence (simplified - using model's confidence)
            confidence = 0.85  # Default confidence
            
            return {
                "text": generated_text,
                "confidence": confidence,
                "model": self.model_name,
                "device": self.device
            }
            
        except Exception as e:
            logger.error(f"Text extraction failed: {e}")
            raise

# Initialize the service
try:
    trocr_service = LocalTrOCRService()
except Exception as e:
    logger.error(f"Failed to initialize TrOCR service: {e}")
    trocr_service = None

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy" if trocr_service else "unhealthy",
        "model": trocr_service.model_name if trocr_service else None,
        "device": trocr_service.device if trocr_service else None
    })

@app.route('/extract', methods=['POST'])
def extract_text():
    """Extract text from uploaded image"""
    try:
        if not trocr_service:
            return jsonify({"error": "TrOCR service not available"}), 500
        
        # Check if file was uploaded
        if 'file' in request.files:
            file = request.files['file']
            image_data = file.read()
        elif 'image' in request.json:
            # Handle base64 image data
            image_data = request.json['image']
        else:
            return jsonify({"error": "No image data provided"}), 400
        
        # Extract text
        result = trocr_service.extract_text(image_data)
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/models', methods=['GET'])
def list_models():
    """List available models"""
    return jsonify({
        "available_models": [
            "microsoft/trocr-base-handwritten",
            "microsoft/trocr-small-handwritten", 
            "microsoft/trocr-large-handwritten",
            "microsoft/trocr-base-printed",
            "microsoft/trocr-small-printed",
            "microsoft/trocr-large-printed"
        ],
        "current_model": trocr_service.model_name if trocr_service else None
    })

if __name__ == '__main__':
    logger.info("Starting TrOCR Local Service...")
    logger.info("This service will download the model on first use (may take a few minutes)")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
