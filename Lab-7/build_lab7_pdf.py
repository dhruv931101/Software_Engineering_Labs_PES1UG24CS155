"""Build and verify the Lab 7 report from the four captured terminal images."""

from pathlib import Path
import shutil

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
SCREENSHOTS = ROOT / "screenshots"
PRIMARY_PDF = ROOT / "PES1UG24CS155_Lab7.pdf"
LEGACY_PDF = ROOT / "PES1UG24CS155_Lab7_FuzzTesting.pdf"
PAGE_SIZE = landscape(letter)
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
MARGIN = 36

SHOT_STAGES = [
    (
        "01_original_application.png",
        "1. Original application",
        "The unmodified starter is run with ticket ID <font name='Courier'>TF-2024-0456</font>, "
        "fine values <font name='Courier'>500,1200,300</font>, and reading "
        "<font name='Courier'>72/60</font>. It prints the parsed ticket, 2,000 total fines, "
        "and 20 percent over the limit.",
    ),
    (
        "02_initial_fuzz_failures.png",
        "2. Initial Hypothesis run against the original",
        "The original module was selected with <font name='Courier'>LAB7_USE_ORIGINAL=1</font>. "
        "Pytest collected 14 cases: 10 failed and 4 passed. Failures expose zero-year acceptance, "
        "negative-fine acceptance, incorrect at-or-under-limit behavior, zero-limit division, "
        "and missing type validation.",
    ),
    (
        "03_fixed_application.png",
        "3. Fixed application",
        "The corrected <font name='Courier'>processor.py</font> is run with the same sample inputs. "
        "Its output keeps the valid ticket and fine total while reporting 20 percent over the limit.",
    ),
    (
        "04_final_passing_tests.png",
        "4. Final Hypothesis run against the fixed implementation",
        "The original-module environment switch was cleared. All 14 collected pytest cases passed "
        "against <font name='Courier'>processor.py</font>.",
    ),
]


def make_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "ReportTitle", parent=base["Title"], fontName="Helvetica-Bold",
            fontSize=23, leading=29, textColor=colors.HexColor("#14324a"),
            alignment=TA_LEFT, spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle", parent=base["Normal"], fontName="Helvetica",
            fontSize=12, leading=17, textColor=colors.HexColor("#3e5e75"),
            spaceAfter=12,
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Heading2"], fontName="Helvetica-Bold",
            fontSize=13, leading=17, textColor=colors.HexColor("#14324a"),
            spaceBefore=8, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName="Helvetica",
            fontSize=9.5, leading=13, textColor=colors.HexColor("#202b33"),
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["BodyText"], fontName="Helvetica",
            fontSize=8.2, leading=10.5, textColor=colors.HexColor("#202b33"),
        ),
        "stage": ParagraphStyle(
            "Stage", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=16, leading=20, textColor=colors.HexColor("#14324a"),
            spaceAfter=5,
        ),
        "caption": ParagraphStyle(
            "Caption", parent=base["BodyText"], fontName="Helvetica",
            fontSize=9, leading=12, textColor=colors.HexColor("#354a59"),
            spaceAfter=9,
        ),
        "table_head": ParagraphStyle(
            "TableHead", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=8.5, leading=10.5, textColor=colors.white,
        ),
        "table_body": ParagraphStyle(
            "TableBody", parent=base["BodyText"], fontName="Helvetica",
            fontSize=8, leading=10.3, textColor=colors.HexColor("#202b33"),
        ),
    }


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d6e0e7"))
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, 27, PAGE_WIDTH - MARGIN, 27)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#536a79"))
    canvas.drawString(MARGIN, 15, "PES University Software Engineering  |  Lab 7")
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 15, f"Dhruv Swatantramath  |  Page {doc.page}")
    canvas.restoreState()


def build_report(output_path):
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=PAGE_SIZE,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=30,
        bottomMargin=40,
        title="PES University Software Engineering Lab 7 — Fuzzing for Input Validation Bugs",
        author="Dhruv Swatantramath (PES1UG24CS155)",
        subject="Traffic Fine property-based testing report",
    )

    story = [
        Paragraph("Lab 7 — Fuzzing for Input Validation Bugs", styles["title"]),
        Paragraph("Software Engineering · Traffic Fine input processor", styles["subtitle"]),
    ]

    identity = [
        [Paragraph("STUDENT", styles["table_head"]), Paragraph("SRN", styles["table_head"]), Paragraph("PROJECT", styles["table_head"]), Paragraph("RUNTIME", styles["table_head"])],
        [Paragraph("Dhruv Swatantramath", styles["table_body"]), Paragraph("PES1UG24CS155", styles["table_body"]), Paragraph("Traffic Fine", styles["table_body"]), Paragraph("Python 3.13.15", styles["table_body"])],
    ]
    identity_table = Table(identity, colWidths=[2.25 * inch, 1.8 * inch, 1.8 * inch, 1.5 * inch])
    identity_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#214b66")),
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#edf3f7")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c7d4dd")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c7d4dd")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [identity_table, Spacer(1, 8)]
    story += [
        Paragraph("Tested functions and properties", styles["section"]),
    ]
    functions = [
        [Paragraph("FUNCTION", styles["table_head"]), Paragraph("HYPOTHESIS COVERAGE", styles["table_head"])],
        [Paragraph("<font name='Courier'>parse_ticket_id</font>", styles["table_body"]), Paragraph("Normalizes valid identifiers; rejects zero year and malformed separators; shared None-type check.", styles["table_body"])],
        [Paragraph("<font name='Courier'>total_fines</font>", styles["table_body"]), Paragraph("Sums and caps generated non-negative amounts; handles empty input; rejects negative and malformed tokens; shared None-type check.", styles["table_body"])],
        [Paragraph("<font name='Courier'>speed_excess</font>", styles["table_body"]), Paragraph("Checks integer percentage relation and non-negative output; rejects zero limit, negative speed, malformed readings; shared None-type check.", styles["table_body"])],
    ]
    function_table = Table(functions, colWidths=[1.65 * inch, 8.1 * inch], repeatRows=1)
    function_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#214b66")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f6f8")]),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c7d4dd")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c7d4dd")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story += [function_table, Spacer(1, 6)]
    story += [
        Paragraph("Workflow and verified results", styles["section"]),
        Paragraph(
            "The unmodified starter was kept as <font name='Courier'>processor_original.py</font>. "
            "The same Hypothesis suite selects it with <font name='Courier'>LAB7_USE_ORIGINAL=1</font> "
            "for the baseline, then runs against the corrected <font name='Courier'>processor.py</font>. "
            "The baseline collected 14 test cases (10 failed, 4 passed). The final run collected 14 "
            "and passed all 14. The examples use Python 3.13.15, pytest 9.2.0, and Hypothesis 6.170.15.",
            styles["body"],
        ),
        Paragraph(
            "The fix validates input types and formats, rejects a zero ticket year and negative fines, "
            "treats blank fine input as zero, requires a positive speed limit, and returns zero when "
            "speed is at or below the limit.",
            styles["body"],
        ),
        PageBreak(),
    ]

    image_width = PAGE_WIDTH - 2 * MARGIN
    for index, (filename, title, caption) in enumerate(SHOT_STAGES):
        image_path = SCREENSHOTS / filename
        if not image_path.is_file():
            raise FileNotFoundError(f"Required genuine screenshot missing: {image_path}")
        screenshot = Image(str(image_path))
        ratio = screenshot.imageHeight / screenshot.imageWidth
        screenshot.drawWidth = image_width
        screenshot.drawHeight = image_width * ratio
        story += [
            Paragraph(title, styles["stage"]),
            Paragraph(caption, styles["caption"]),
            Spacer(1, 4),
            screenshot,
        ]
        if index != len(SHOT_STAGES) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)

    reader = PdfReader(str(output_path))
    if len(reader.pages) != 5:
        raise RuntimeError(f"Expected 5 pages, found {len(reader.pages)}")
    cover_text = reader.pages[0].extract_text() or ""
    for required in ("Dhruv Swatantramath", "PES1UG24CS155", "Traffic Fine", "Fuzzing for Input Validation Bugs"):
        if required not in cover_text:
            raise RuntimeError(f"PDF cover is missing required text: {required}")
    for page_number, page in enumerate(reader.pages[1:], start=2):
        if len(page.images) != 1:
            raise RuntimeError(f"Expected one screenshot on page {page_number}, found {len(page.images)}")
    print(f"Built {output_path.name}: {len(reader.pages)} pages, four embedded screenshots, student details verified.")


if __name__ == "__main__":
    build_report(PRIMARY_PDF)
    shutil.copyfile(PRIMARY_PDF, LEGACY_PDF)
    print(f"Updated compatibility filename: {LEGACY_PDF.name}")
