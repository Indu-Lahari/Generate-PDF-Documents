from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)            #so pages won't break

for index, row in df.iterrows():
    pdf.add_page()
    #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)

    #Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    pdf.set_text_color(180, 180, 180)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        pdf.set_text_color(180, 180, 180)

pdf.output("output.pdf")