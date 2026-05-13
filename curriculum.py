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
        self.RIGHT_X = self.SIDEBAR_WIDTH + self.MARGIN_X
        self.RIGHT_WIDTH = self.pdf.w - self.SIDEBAR_WIDTH - (2 * self.MARGIN_X)

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
            "Courses": [
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
            ],
            "exp": [
                {
                    "name": "Vectralis",
                    "time": "2 years 2 months",
                    "language": "Python (Django), Angular, React, PostgreSQL",
                    "position": "Full Stack Developer",
                    "description": "Led the design and implementation of robust, scalable architectures for industrial monitoring systems. My role spanned from creating intuitive, dynamic user interfaces to implementing complex backend business logic, ensuring high-performance communication via ORMs and PostgreSQL query optimization.",
                    "projects": [
                        {
                            "name": "BCS (Business Control System)",
                            "description": "Full-cycle developer for industrial applications. Specialized in frontend modernization (Angular to React) and backend optimization using Python/Django. Expert in transforming complex production data into real-time visualization solutions and automated reporting systems for strategic decision-making."
                        }
                    ]
                },
                {
                    "name": "Busmen",
                    "time": "2 years 7 months",
                    "language": "Python (Django), PHP",
                    "position": "Full Stack Developer",
                    "description": "Strategically evolved the biometric management system from fragmented, isolated device administration into a unified, automated middleware architecture based on Django. This transition was key to eliminating technical debt from manual synchronization and ensuring data integrity across corporate infrastructure, setting an efficiency standard in IoT integration.\n\nKey Engineering Achievements:\n- Middleware Architecture & Data Unification (Single Source of Truth): Designed and implemented a centralized middleware for managing 18+ ZKTeco biometric devices, bi-directionally integrated with the corporate ERP. This established absolute data parity and optimized attendance processing times.\n- Hardware Integration & Low-Level Communication: Architected solutions for direct communication with biometric terminals using ZK SDKs and network protocols (sockets). Developed a mass synchronization engine ensuring consistency for fingerprint templates and user profiles.\n- Proactive Monitoring & Connectivity Management: Implemented a real-time monitoring system using the Singleton design pattern for connection management, ensuring high availability and immediate response to hardware or network failures.\n- Rule Engine for Attendance & Incidents: Developed advanced business logic for processing biometric logs, integrating backend services for dynamic calculation of attendance, delays, and absences, adapting in real-time to ERP incident calendars.\n- Security & Privilege Management: Designed high-priority modules for user administration and access levels, ensuring segmented security management according to employee profiles.",
                    "projects": [
                        {
                            "name": "Time Check",
                            "description": "IoT integration platform (Python/Django) centralizing 18 biometric terminals. Responsible for the identity synchronization engine, low-level SDK communication, and seamless integration with the 'Busmen' ERP via RESTful services. Focused on concurrent connection optimization and system scalability."
                        }
                    ]
                },
                {
                    "name": "GEOVOY",
                    "time": "2 years 7 months",
                    "language": "Kotlin, Flutter, Dart",
                    "position": "Cross-Platform Mobile Developer",
                    "description": "Led the strategic evolution of the mobile ecosystem, transforming a fragmented native development model into a unified cross-platform architecture. This transition resolved technical debt from maintaining separate codebases and eliminated UI/UX inconsistencies.\n\nKey Engineering Achievements:\n- Strategic Migration & Product Unification: Directed the migration of native apps to an advanced cross-platform framework, establishing a 'Single Source of Truth'. This ensured absolute UI/UX parity between Android and iOS, optimizing deployment times by 50%.\n- Geolocation & Real-Time Tracking: Architected and implemented high-precision tracking solutions using WebSockets and background persistence services for seamless logistics monitoring.\n- Route Optimization & Dynamic ETA: Integrated advanced geofencing logic and direction engines for dynamic Estimated Time of Arrival (ETA) calculation, adapting in real-time to route variables.\n- Security & Critical Response: Developed high-priority safety modules, including immediate alert systems and panic buttons integrated with backend services, designed under high-availability principles.\n- Notification Infrastructure: Implemented a robust push communication system for managing critical events, route changes, and service updates, ensuring efficient information delivery.",
                    "projects": [
                        {
                            "name": "Busmen Rutas (PA)",
                            "description": "Mission-critical logistics solution for personnel transport. Implemented a robust Kotlin architecture with multi-server support, asynchronous synchronization via Coroutines, and an optimized UX using CameraX and local persistence.",
                            "country": "Panama",
                            "shop": "https://play.google.com/store/apps/details?id=busmenapps.busmen.copatierra"
                        },
                        {
                            "name": "Servicio Busmen (PA)",
                            "description": "Enterprise mobility platform for real-time transport network orchestration. Architected an offline-first model using Kotlin and hybrid persistence (Room/Realm), ensuring telemetry data integrity via Google Maps SDK and QR identity validation.",
                            "country": "Panama",
                            "shop": "https://play.google.com/store/apps/details?id=com.geovoy.serviciobusmenpa"
                        },
                        {
                            "name": "PITWALL",
                            "description": "Real-time vehicle asset monitoring system. Developed dynamic dashboards using Kotlin and Coroutines to process critical telemetry (mileage, fuel ranges, predictive maintenance) and streamlined service order generation (Pre-ODTs).",
                            "country": "Mexico",
                            "shop": "https://play.google.com/store/apps/details?id=com.geovoy.pitwall"
                        },
                        {
                            "name": "Rutas Busmen (MX)",
                            "description": "Robust system for transport auditing and operation. Led the implementation of an MVVM architecture with Clean Architecture in Kotlin, ensuring modular scalability for surveys, suggestions, and profile management.",
                            "country": "Mexico",
                            "shop": "Not published"
                        },
                        {
                            "name": "Busmen (MX)",
                            "description": "Enterprise-level security and operation system for personnel transport. Led a modular MVVM architecture, separating business logic from UI for modules like dynamic QR access passes and real-time incident management.",
                            "country": "Mexico",
                            "shop": "https://play.google.com/store/apps/details?id=com.geovoy.geovoy_app"
                        },
                        {
                            "name": "Rastreo Busmen",
                            "description": "Real-time monitoring and security system built with Flutter. Implemented a modular MVVM architecture and a hybrid REST/WebSocket engine for live telemetry processing and video streaming (VMS) integration.",
                            "country": "Mexico",
                            "shop": "https://play.google.com/store/apps/details?id=com.geovoy.geo_rastreo"
                        },
                        {
                            "name": "Inplants",
                            "description": "Specialized platform for digitalizing 'Inplant' supervision. Integrated Traccar API for GPS telemetry cross-referencing and developed a custom synchronization engine for offline occupancy and punctuality metrics capture.",
                            "country": "Mexico",
                            "shop": "https://play.google.com/store/apps/details?id=com.geovoy.inplant"
                        },
                        {
                            "name": "Instaladores",
                            "description": "Technical ecosystem for telematics hardware installation auditing. Developed a modular architecture with an offline-first persistence strategy and async sync queues for real-time diagnostic validations.",
                            "country": "Mexico",
                            "shop": "Internal App"
                        }
                    ]
                }
            ],
            "exp_personal":[
                {
                    "name":"Purchasing Administrator",
                    "stack": "Python (Django), kotlin, flutter, NGNX, EC2 Amazon, WSGI",
                    "description": '''"As part of my personal initiative, I developed a comprehensive financial and operational management platform designed to solve information fragmentation caused by the use of multiple credit lines and deferred payment schemes. The system centralizes complex liabilities, recurring expenses, and cash disbursements, enabling accurate monthly cash flow projections and supporting data-driven financial decision-making based on consolidated information.Additionally, the ecosystem includes a logistics control module for preventive vehicle maintenance and fuel performance monitoring, as well as a collaborative resource planning system with a dual-approval workflow, ensuring status validation among multiple users before task execution."'''
                }
            ]
        }
        self.pdf.set_font("Helvetica", size=12)

    def build_cv(self):

        self.create_line(self.SIDEBAR_WIDTH, 0, self.SIDEBAR_WIDTH, self.pdf.h)

        img_w = self.SIDEBAR_WIDTH * 0.8
        img_x = (self.SIDEBAR_WIDTH - img_w) / 2
        # self.pdf.image("profile.jpeg", x=img_x, y=2, w=img_w)

        # Información Personal en la barra lateral
        self.pdf.set_y(10)
        info = self.datos_cv["info_personal"]
        self.create_text_auto(info["name"], size=14, style="B")
        self.pdf.ln(2)
        self.create_text_auto(info["street"], size=9)
        self.create_text_auto(info["email"], size=9)

        self.pdf.set_y(65)

        self.draw_section_title("Education")
        for edu in self.datos_cv[ "education" ]:
            self.create_text_auto( edu, size=10 )
            self.pdf.ln(2)

        self.draw_section_title("Languages")
        for lang in self.datos_cv[ "language" ]:
            self.create_text_auto( lang, size=10 )

        self.pdf.ln(1)

        self.draw_section_title("Courses")
        for curso in self.datos_cv[ "Courses" ]:
            self.create_text_auto(f"- {curso}", size=9)
            self.pdf.ln(1)

        # Columna Derecha: Experiencia Profesional
        self.pdf.set_xy(self.RIGHT_X, 20)
        self.create_title_jobs("PROFESSIONAL EXPERIENCE")
        self.pdf.ln(2)

        for job in self.datos_cv["exp"]:
            self.create_text_jobs(job["position"], style="B", size=11)
            self.create_text_jobs(f"{job['name']} | {job['time']}", size=10, style="I")
            self.create_text_jobs(f"Technologies: {job['language']}", size=9, style="B")
            self.pdf.ln(1)
            self.create_text_jobs(job["description"], size=9)
            self.pdf.ln(2)
            for project in job["projects"]:
                self.create_text_jobs(f"- Project: {project['name']}", size=9, style="B")
                self.create_text_jobs(project["description"], size=9)
                self.pdf.ln(1)
            self.pdf.ln(3)

        self.create_title_jobs("PERSONAL EXPERIENCE")
        self.pdf.ln(2)
        for job in self.datos_cv["exp_personal"]:
            self.create_text_jobs(f"{job['name']}", size=10, style="I")
            self.create_text_jobs(f"Technologies: {job['stack']}", size=9, style="B")
            self.create_text_jobs(job["description"], size=9)
            self.pdf.ln(2)

    def draw_section_title( self, title ):
        self.pdf.set_font( "Helvetica", "B", 12 )
        self.pdf.set_x( self.MARGIN_X )
        self.pdf.cell( self.SIDEBAR_WIDTH - 10, 10, title, new_x="LMARGIN", new_y="NEXT" )

    def create_text_auto(self, text, size=10, style=""):
        self.pdf.set_font("Helvetica", style=style, size=size)
        self.pdf.set_x(self.MARGIN_X)
        self.pdf.multi_cell(w=self.SIDEBAR_WIDTH - 10, h=5, text=text, align="L")

    def create_title_jobs(self, title):
        self.pdf.set_font("Helvetica", "B", 12)
        self.pdf.set_x(self.RIGHT_X)
        self.pdf.cell(
            self.RIGHT_WIDTH,
            10,
            title,
            new_x="LEFT",
            new_y="NEXT"
        )

    def create_text_jobs(self, text, size=10, style=""):
        self.pdf.set_font("Helvetica", style=style, size=size)
        self.pdf.set_x(self.RIGHT_X)
        self.pdf.multi_cell(
            w=self.RIGHT_WIDTH,
            h=5,
            text=text,
            align="L"
        )


    def create_line(self, x1, y1, x2, y2):

        self.pdf.line( x1, y1, x2, y2 )

    def create_cv_pdf(self, path):
        self.pdf.output( path )

if __name__ == "__main__":
    cv = Curriculum()
    cv.build_cv()
    cv.create_cv_pdf("archivo.pdf")