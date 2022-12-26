from fpdf import FPDF


name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.image("shirtificate.png", x=0, y=60)
pdf.set_font("Helvetica", size=48)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")
pdf.set_x(0)
pdf.set_y(0)
pdf.set_font("Helvetica", size=24)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 275, f"{name} took CS50", align='C')
pdf.output("shirtificate.pdf")