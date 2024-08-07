# PDF Document Generator

## Project Description

The PDF Document Generator is a tool designed to create customized PDF documents based on data from a CSV file. This project reads topics and page counts from a CSV file and generates a PDF document with a specific layout, including headers, footers, and lined pages.

## Process

1. **Data Input:**
   - Read data from `topics.csv` using Pandas. The CSV file contains information on different topics and the number of pages required for each topic.

2. **PDF Creation:**
   - Initialize a PDF object using the FPDF library with A4 size pages.
   - Disable automatic page breaks and set margins to zero for custom layout control.

3. **Content Layout:**
   - For each topic in the CSV, create a new page in the PDF.
   - Set the topic as the header on each page.
   - Add lines to create a lined page effect.
   - Set the footer with the topic name.
   - For topics requiring multiple pages, add additional pages as needed with the same layout.

4. **Output:**
   - Save the generated PDF document as `output.pdf`.

## Technology Used

- **FPDF:** A library for generating PDF documents in Python.
- **Pandas:** A library used to handle CSV data and iterate over rows.
- **Python:** The programming language used for scripting the PDF generation.

## What I Learned

- **PDF Generation:**
  - Gained experience in using the FPDF library to create and format PDF documents programmatically.
  - Learned how to set custom headers, footers, and add lines to the PDF for visual formatting.

- **Data Handling:**
  - Developed skills in reading and processing data from CSV files using Pandas.
  - Implemented logic to dynamically generate multiple pages based on data.

- **Programming Techniques:**
  - Improved understanding of Python scripting for file handling and document generation.
  - Applied knowledge of loops and conditional statements to customize the PDF output.

## Future Insights

- **Customization:**
  - Enhance the PDF generation with additional features such as customizable fonts, colors, and page sizes.
  - Add support for different document formats and layouts based on user input.

- **User Interface:**
  - Develop a graphical user interface (GUI) to allow users to input data and generate PDFs without needing to modify the CSV file manually.

- **Error Handling:**
  - Implement better error handling for cases where the CSV file is missing or has incorrect data formats.
  - Provide user feedback and validation checks for the input data.

- **Integration:**
  - Explore integration with other tools and libraries for advanced PDF functionalities, such as embedding images or tables.

Feel free to explore the code to understand how the PDF documents are generated and formatted:
- `main.py` for the core functionality of PDF creation.

Happy coding!