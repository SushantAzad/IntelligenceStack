# IntelligenceStack

A Python-based intelligence toolkit that combines web scraping with OpenAI's language models for extracting, processing, and analyzing web content. This project leverages modern NLP capabilities to intelligently parse and understand website data.

## Overview

IntelligenceStack is a comprehensive toolkit designed to:

- **Scrape Web Content**: Extract text, metadata, and links from websites efficiently
- **Integrate with OpenAI API**: Process scraped content using GPT models for intelligent analysis
- **Manage Tokens**: Monitor and optimize token usage with built-in tiktoken integration
- **Handle Requests**: Manage HTTP requests with proper headers and error handling

## Features

✨ **Web Scraping**

- Extract website titles and cleaned text content
- Retrieve links from webpages
- Automatic removal of irrelevant elements (scripts, styles, images)
- Content truncation for efficient processing (2,000 character limit)

🤖 **AI Integration**

- OpenAI API integration for intelligent content analysis
- Support for GPT models
- Token counting and optimization

📊 **Data Processing**

- Markdown support for formatted content
- Request management with proper HTTP headers
- Python 3.12+ compatibility

## Project Structure

```
IntelligenceStack/
├── main.py                      # Main entry point
├── scraper.py                   # Web scraping utilities
├── openai_api.ipynb            # OpenAI API integration examples
├── brocherForCompanies.ipynb   # Broker/Company data processing
├── Request_module.ipynb        # Request handling module
├── tiktoken.ipynb              # Token counting examples
├── test.ipynb                  # Testing utilities
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## Dependencies

- **beautifulsoup4** (>=0.0.2) - HTML/XML parsing and scraping
- **requests** (>=2.34.2) - HTTP requests library
- **openai** (>=2.41.1) - OpenAI API client
- **tiktoken** (>=0.13.0) - Token counting for OpenAI models
- **python-dotenv** (>=1.2.2) - Environment variable management
- **markdown** (>=3.10.2) - Markdown processing
- **ipykernel** (>=7.3.0) - Jupyter kernel support

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd IntelligenceStack
```

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -e .
```

Or manually install with:

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
   Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Web Scraping

```python
from scraper import fetch_website_contents, fetch_website_links

# Extract website content
content = fetch_website_contents("https://example.com")
print(content)

# Extract links from website
links = fetch_website_links("https://example.com")
print(links)
```

### Running the Project

```bash
python main.py
```

## Key Modules

### scraper.py

Provides web scraping utilities:

- `fetch_website_contents(url)` - Retrieves and cleans website text
- `fetch_website_links(url)` - Extracts all links from a webpage

### Jupyter Notebooks

Interactive development and experimentation:

- **openai_api.ipynb** - Examples of OpenAI API integration
- **brocherForCompanies.ipynb** - Specialized broker/company data extraction
- **tiktoken.ipynb** - Token counting demonstrations
- **test.ipynb** - Testing and validation examples

## Configuration

The project uses `pyproject.toml` for configuration management following Python packaging standards. Key settings:

- Project name: `intelligencestack`
- Version: `0.1.0`
- Python requirement: `>=3.12`

### Environment Variables

Configure the following in your `.env` file:

```env
OPENAI_API_KEY=your_key_here
```

## Development

### Project Structure Best Practices

- Use virtual environments for isolation
- Follow PEP 8 style guidelines
- Document complex functions and modules
- Test code in Jupyter notebooks before production use

### Running Tests

Execute test notebooks:

```bash
jupyter notebook test.ipynb
```

## API Integration

The project includes OpenAI API integration for:

- Content analysis and summarization
- Data extraction and classification
- Intelligent processing of scraped content

Refer to `openai_api.ipynb` for detailed examples.

## Performance Considerations

- **Content Truncation**: Website content is limited to 2,000 characters for efficiency
- **Token Optimization**: Use tiktoken to monitor token usage and manage costs
- **Request Headers**: Proper User-Agent headers are configured to avoid blocking

## Future Enhancements

- Caching mechanism for frequently accessed websites
- Multi-threaded scraping for improved performance
- Database integration for content storage
- Advanced error handling and retry logic
- Comprehensive logging system
- API endpoints for programmatic access

## License

[Specify your license here]

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For issues, questions, or suggestions, please open an issue in the repository.

## Changelog

### v0.1.0 (Current)

- Initial project setup
- Web scraping utilities
- OpenAI API integration foundation
- Jupyter notebook examples
