from fpdf import FPDF
from fpdf.enums import XPos, YPos

class Curriculum():

    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()

        # 1. Definimos constantes de diseño (Evitamos números mágicos)
        self.SIDEBAR_WIDTH = self.pdf.w / 3
        self.MARGIN_X = 5
        self.LINE_SPACING = 8

        self.datos_cv = {
            "info_personal": {
                "name": "Daniel Hernández Palagot",
                "street": "Tlajomulco de Zuñiga, Gdl, JAl - 3332070550",
                "email": "danielpalagot96@gmail.com"
            },
            "education": [
                "Bachelor's Degree: COABEJ #10 C. Constitución 10, Villas del Eden, 45650 San Sebastián el Grande, Jal.",
                "Higher Education: Instituto Tecnológico de Tlajomulco Km 10 carr Tlajomulco, Cto. Metropolitano Sur, 45640 Tlajomulco de Zúñiga, Jal."
            ],
            "Courses":[
                "Introduction to cyber segurity 05/2020",
                "Database Administrator - 12/2020",
                "Master in Python Django, Flask, Tkinter, and SQL - 09/2021",
                "Python for Android, iOS, Windows, Linux, and MacOS - 02/2021",
                "REST API Web Services with Python 3 and MySQL - 02/2021",
                "Data Science Fundamentals - 03/2025",
                "Data Science Fundamentals - 03/2025",
                "React: From Zero to Expert - 06/2025",
                "Android 14 Course with Kotlin: Intensive and Practical - 06/2024"
            ],
            "language": [
                "ESPAÑOL Nativo",
                "INGLES B1 - En progreso"
            ]
        }
        self.pdf.set_font("Helvetica", size=12)

    def build_cv(self):

        self.create_line(self.SIDEBAR_WIDTH, 0, self.SIDEBAR_WIDTH, self.pdf.h)

        img_w = self.SIDEBAR_WIDTH * 0.8
        img_x = (self.SIDEBAR_WIDTH - img_w) / 2
        self.pdf.image("profile.jpeg", x=img_x, y=2, w=img_w)

        self.pdf.set_y(65)

        self.draw_section_title("Education")
        for edu in self.datos_cv["education"]:
            self.create_text_auto(edu, size=12)
            self.pdf.ln(2)

        self.draw_section_title("Languages")
        for lang in self.datos_cv["language"]:
            self.create_text_auto(lang, size=12)

        self.pdf.ln(1)

        self.draw_section_title("Courses")
        for curso in self.datos_cv["Courses"]:
            self.create_text_auto(f"- {curso}", size=12)
            self.pdf.ln(1)

    def draw_section_title( self, title ):
        self.pdf.set_font( "Helvetica", "B", 12 )
        self.pdf.set_x( self.MARGIN_X )
        self.pdf.cell( self.SIDEBAR_WIDTH - 10, 10, title, new_x="LMARGIN", new_y="NEXT" )

    def create_text_auto(self, text, size=10, style=""):
        self.pdf.set_font("Helvetica", style=style, size=size)
        self.pdf.set_x(self.MARGIN_X)
        self.pdf.multi_cell(w=self.SIDEBAR_WIDTH - 10, h=5, text=text, align="L")


    def create_line(self, x1, y1, x2, y2):

        self.pdf.line( x1, y1, x2, y2 )

    def create_cv_pdf(self, path):
        self.pdf.output( path )

if __name__ == "__main__":
    cv = Curriculum()
    cv.build_cv()
    cv.create_cv_pdf("/Users/dya/Documents/proyects/CV/archivo.pdf")