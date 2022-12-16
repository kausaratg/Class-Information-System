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
        "Computer Science Group C Timetable ",
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


def timetable_d(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = [
        "Computer Science Group D Timetable ",
        " ",
        "Monday",
        "8:00am-9:00am Phy101 SCLT",
        "10:00am-11:00am GEDS 105",
        "11:00am-12:00pm CHEM 101(WRA/SCLT)",
        "2:00pm-4:00pm STAT 101 A008/A007",
        "4:00pm-6:00pm GEDS 101",
        "  ",
        "Tuesday",
        "9:00am-10:00am GEDS 101(Amphitheatre)",
        "10:00am-11:00am CHEM 101 (WRA/SCLT)",
        "11:00am-1:00pm GEDS 131",
        "2:00pm-3:00pm Phy 101 (SCLT)",
        " ",
        "Wednesday",
        "9:00am-11:00am COSC 111 G1(E102)",
        "11:00am-1:00pm COSC 111 G2(R1/8)",
        "2:00pm-3:00pm  COSC 111 G2(R1/8)",
        " ",
        "Thursday",
        "7:00am-9:00am COSC 107 (NH S4)",
        "9:00am-11:00am GEDS 107",
        "12:00am-1:00pm Chem Practical (D004)",
        " ",
        "Friday",
        "8:00am-9:00am COSC 111 G1 (E102)",
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="Group D timetable.pdf")


def timetable_a(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 13)

    lines = [
        "Computer Science Group A Timetable ",
        " ",
        "Monday",
        "7:00am-9:00am STAT 101 SCLT",
        "10:00am-11:00am GEDS 105",
        "11:00am-12:00pm PHY101 B107",
        "2:00pm-4:00pm CHEM 101 B007",
        "4:00pm-6:00pm GEDS 101",
        "  ",
        "Tuesday",
        "9:00am-10:00am Chapel Seminar(Amphitheatre)",
        "10:00am-11:00am CHEM 101 (A008)",
        "11:00am-1:00pm GEDS 131",
        "4:00pm-6:00pm MATH 101 B006",
        " ",
        "Wednesday",
        "7:00am-9:00am COSC 107 NH Studio 4",
        "11:00am-12:00pm MATH 101 B106",
        "12:00pm-1:00pm  CHEM 101 PRACTICAL D004",
        "3:00pm-4:00pm COSC 111(GRP 2) NH ROOM2",
        " ",
        "Thursday",
        "9:00am-11:00am GEDS 107",
        "11:00am-12:00pm COSC 111 GR1/NELE 202 ",
        "2:00pm-4:00pm COSC 111 GR2 BUCODEL LAB 5"
        " ",
        "Friday",
        "8:00am-10:00am PHY 101 SCLT",
        "12:00pm-1:00pm COSC 111 GR1 F202",  
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="Group A timetable.pdf")

def timetable_b(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 13)

    lines = [
        "Computer Science Group B Timetable ",
        " ",
        "Monday",
        "7:00am-9:00am CHEM 107 B007",
        "10:00am-11:00am GEDS 105",
        "11:00am-1:00pm MATH 101 D104",
        "2:00pm-4:00pm PHY 101 F105",
        "4:00pm-6:00pm GEDS 101",
        "  ",
        "Tuesday",
        "9:00am-10:00am Chapel Seminar(Amphitheatre)",
        "11:00am-12:00pm GEDS 131",
        "12:00pm-1:00pm COSC111 GROUP E2O2",
        "2:oopm-3:00pm MATH 101 B007",
        "3:00pm-5:00pm STAT 101 BUCODEL",
        " ",
        "Wednesday",
        "2:00pm-3:00pm PHY 101 B007",
        "3:00pm-4:00pm COSC 111 GROUP 2 PRACT NEW HORIZON(ROOM 1)",
        "4:00pm-6:00pm COSC 107 STUDIO 4",
        " ",
        "Thursday",
        "8:00am-9:00am CHEM 101 B006",
        "9:00am-11:00am GEDS 107 ",
        "11:00am-12:00pm CHEM 101 PRACTICAL BOO7",
        "2:00pm-3:00pm COSC 111 GROUP 1 E202",
        "2:00PM-4:00PM COSC 111 GROUP 2 A112",
        " ",
        "Friday",
        "9:00am-10:00am COSC 111 GROUP 1 PRACTICAL", 
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="Group B timetable.pdf")