from django.shortcuts import render
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
def timetable(request):
    return render(request, "timetable/timetable.html")

def timetable_c(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = [
        "Computer Science Group c Timetable ",
        " ",
        "Monday",
        "8am-8:50am MATH-D007/D104",
        "10am-10:50am GEDS 105",
        "11am-12:50pm COSC 107 New Horizon",
        "2pm-2:50pm Math-D104\D007",
        "4pm-6pm Geds101",
        "  ",
        "Tuesday",
        "8:50am-9:50am BIS Amphitheatre",
        "11am-12:50pm GEDS 131",
        "2pm-3:50pm COSC G1-New Horizon Room 2",
        " ",
        "Wednesday",
        "9am-11:50am Chem 101 B007",
        "12pm-12:50pm COSC G1 practical F104",
        "3pm-3:50pm Phy 101 SCLT/B107",
        " ",
        "Thursday",
        "9am-10:50am GEDS 107",
        "11am-11:50am Math 101 D007/D107",
        "3pm-5pm COSC G2 E202",
        " ",
        "Friday",
        "7am-8:50am Stat 101(B006)",
        "9am-10am COSC G2 F204",
        "11am-12:50pm Phy 101 COSC (B107/SCLT)",
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="Group C timetable.pdf")