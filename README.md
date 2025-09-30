# Mossip OCR - Advanced Text Extraction & Verification

A sophisticated OCR-driven solution that seamlessly extracts text from scanned documents, intelligently auto-fills digital forms, and accurately verifies the extracted data against the original source for enhanced reliability and efficiency.

## 🚀 Features

- **Microsoft TrOCR Integration**: Uses Microsoft's state-of-the-art TrOCR model for superior text recognition
- **Document Upload & Preview**: Support for various image formats and PDFs
- **Intelligent Form Auto-filling**: Automatically populates form fields from extracted text
- **Data Verification**: Comprehensive verification system with confidence scoring
- **Beautiful UI**: Modern, responsive interface built with React and Tailwind CSS
- **Real-time Processing**: Live OCR extraction with progress indicators
- **Export & Integration**: JSON payload export for backend integration

## 🛠️ Technology Stack

- **Frontend**: React 18 + TypeScript
- **Styling**: Tailwind CSS + Framer Motion
- **OCR Engine**: Microsoft TrOCR via Hugging Face API
- **UI Components**: Custom shadcn/ui-inspired components
- **Build Tool**: Vite

## 📋 Prerequisites

- Node.js 18+ 
- npm or yarn
- Hugging Face API key (for TrOCR functionality)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd mossip-ocr
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Get Hugging Face API Key
1. Visit [Hugging Face](https://huggingface.co/settings/tokens)
2. Create an account or sign in
3. Generate a new API token
4. Copy the token for use in the application

### 4. Start Development Server
```bash
npm run dev
```

The application will open at `http://localhost:3000`

## 🔧 Configuration

### API Key Setup
1. Open the application
2. Enter your Hugging Face API key in the "TrOCR Configuration" section
3. Upload a document and click "Run TrOCR" to use Microsoft's model

### Environment Variables (Optional)
Create a `.env` file in the root directory:
```env
VITE_HUGGINGFACE_API_KEY=your_api_key_here
```

## 📖 Usage

### Basic Workflow
1. **Upload Document**: Click "Upload Document" and select an image or PDF
2. **Configure TrOCR**: Enter your Hugging Face API key
3. **Extract Text**: Click "Run TrOCR" to extract text using Microsoft's model
4. **Review & Edit**: Review extracted text and edit form fields as needed
5. **Verify Data**: Use verification tools to validate extracted information
6. **Export**: Export JSON payload for backend integration

### Demo Mode
- Use "Run OCR (Demo)" to see the application in action without an API key
- Demo mode provides sample data for testing the interface

## 🏗️ Project Structure

```
src/
├── components/
│   ├── ui/                 # Reusable UI components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   └── ...
│   └── OCRVerifyDashboard.tsx  # Main OCR dashboard
├── lib/
│   └── utils.ts           # Utility functions
├── App.tsx                # Main application component
├── main.tsx               # Application entry point
└── index.css              # Global styles
```

## 🔌 API Integration

### TrOCR Service
The application integrates with Microsoft's TrOCR model via Hugging Face:
- **Endpoint**: `https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten`
- **Authentication**: Bearer token via Hugging Face API key
- **Input**: Image files (JPEG, PNG, etc.)
- **Output**: Extracted text with confidence scores

### Backend Integration
Export JSON payloads include:
```json
{
  "meta": {
    "filename": "document.jpg",
    "autoValidate": true,
    "model": "microsoft/trocr-base-handwritten"
  },
  "ocrText": "extracted text content",
  "fields": {
    "fullName": "John Doe",
    "email": "john@example.com"
  },
  "confidences": {
    "fullName": 0.98,
    "email": 0.96
  },
  "checks": {
    "formatting": true,
    "completeness": false
  }
}
```

## 🎯 Use Cases

- **Document Processing**: Extract text from scanned forms, invoices, receipts
- **Form Automation**: Auto-fill digital forms from paper documents
- **Data Entry**: Streamline manual data entry processes
- **Compliance**: Verify document authenticity and completeness
- **Archiving**: Digitize and search through paper documents

## 🚀 Production Deployment

### Build for Production
```bash
npm run build
```

### Deploy Options
- **Vercel**: Connect GitHub repository for automatic deployments
- **Netlify**: Drag and drop the `dist` folder
- **AWS S3**: Upload built files to S3 bucket
- **Docker**: Containerize the application

### Environment Considerations
- Set up proper CORS policies for API calls
- Implement rate limiting for TrOCR API usage
- Consider using Azure Computer Vision for production workloads
- Implement proper error handling and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Microsoft Research**: For the TrOCR model
- **Hugging Face**: For providing the model hosting infrastructure
- **Tailwind CSS**: For the beautiful styling framework
- **React Team**: For the amazing frontend framework

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation for common solutions

---

**Built with ❤️ by Mossip Decode Team**
