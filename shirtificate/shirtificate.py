from fpdf import FPDF
class PDF(FPDF):
    pass
def main():
    name = input("Name: ")
    pdf = PDF(orientation="p", unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0,40,"CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png",x=0, y=40, w=200)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=50, y=100, txt=f"{name} took CS50")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()