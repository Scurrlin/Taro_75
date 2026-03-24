#!/usr/bin/env bash
# Generate a printable PDF from Taro_Fast_Track.md.
# Requires: pip3 install reportlab  (already installed)
# Usage:    bash generate_pdfs.sh

set -e
mkdir -p pdfs

python3 -B << 'PYEOF'
import re
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Preformatted, Table, TableStyle,
    Spacer, HRFlowable, KeepTogether,
)

MARGIN = 0.75 * inch
PAGE_W, PAGE_H = letter
CONTENT_W = PAGE_W - 2 * MARGIN

BODY = ParagraphStyle(
    "Body", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=6,
)
H1 = ParagraphStyle(
    "H1", fontName="Helvetica-Bold", fontSize=20, leading=24,
    spaceAfter=4, spaceBefore=4,
)
H2 = ParagraphStyle(
    "H2", fontName="Helvetica-Bold", fontSize=15, leading=19,
    spaceAfter=4, spaceBefore=12, keepWithNext=True,
)
H3 = ParagraphStyle(
    "H3", fontName="Helvetica-Bold", fontSize=12, leading=16,
    spaceAfter=2, spaceBefore=8, keepWithNext=True,
)
QUOTE = ParagraphStyle(
    "Quote", fontName="Helvetica-Oblique", fontSize=10, leading=13,
    leftIndent=14, textColor=HexColor("#444444"), spaceAfter=4,
)
CODE_STYLE = ParagraphStyle(
    "Code", fontName="Courier", fontSize=8, leading=10,
)
CELL = ParagraphStyle("Cell", fontName="Helvetica", fontSize=8.5, leading=11)
CELL_H = ParagraphStyle("CellH", fontName="Helvetica-Bold", fontSize=8.5, leading=11)


def md_inline(text):
    """Convert markdown inline formatting to ReportLab XML markup."""
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r'<font name="Courier" size="8">\1</font>', text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"<u>\1</u>", text)
    return text


def make_code_block(code_text):
    pre = Preformatted(code_text, CODE_STYLE)
    wrapper = Table([[pre]], colWidths=[CONTENT_W - 12])
    wrapper.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), HexColor("#f5f5f5")),
        ("BOX", (0, 0), (0, 0), 0.5, HexColor("#dddddd")),
        ("TOPPADDING", (0, 0), (0, 0), 8),
        ("BOTTOMPADDING", (0, 0), (0, 0), 8),
        ("LEFTPADDING", (0, 0), (0, 0), 10),
        ("RIGHTPADDING", (0, 0), (0, 0), 10),
    ]))
    return KeepTogether([wrapper, Spacer(1, 4)])


def make_table(rows):
    data = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if all(set(c.strip()) <= set("-: ") for c in cells):
            continue
        data.append(cells)
    if not data:
        return None
    ncols = len(data[0])
    col_w = [CONTENT_W / ncols] * ncols
    tdata = []
    for i, row_cells in enumerate(data):
        style = CELL_H if i == 0 else CELL
        tdata.append([Paragraph(md_inline(c), style) for c in row_cells])
    t = Table(tdata, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f0f0f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#fafafa")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


with open("Taro_Fast_Track.md") as f:
    lines = f.readlines()

story = []
i = 0
while i < len(lines):
    line = lines[i].rstrip("\n")

    if line.startswith("```"):
        code_lines = []
        i += 1
        while i < len(lines) and not lines[i].rstrip("\n").startswith("```"):
            code_lines.append(lines[i].rstrip("\n"))
            i += 1
        i += 1
        story.append(make_code_block("\n".join(code_lines)))
        continue

    if line.startswith("|"):
        table_rows = [line]
        i += 1
        while i < len(lines) and lines[i].rstrip("\n").startswith("|"):
            table_rows.append(lines[i].rstrip("\n"))
            i += 1
        t = make_table(table_rows)
        if t:
            story.append(t)
            story.append(Spacer(1, 6))
        continue

    if line.startswith("### "):
        story.append(Paragraph(md_inline(line[4:]), H3))
        i += 1
        continue
    if line.startswith("## "):
        story.append(Paragraph(md_inline(line[3:]), H2))
        i += 1
        continue
    if line.startswith("# "):
        story.append(Paragraph(md_inline(line[2:]), H1))
        i += 1
        continue

    if line.strip() == "---":
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#cccccc")))
        story.append(Spacer(1, 4))
        i += 1
        continue

    if line.startswith("> "):
        story.append(Paragraph(md_inline(line[2:]), QUOTE))
        i += 1
        continue

    if not line.strip():
        i += 1
        continue

    story.append(Paragraph(md_inline(line), BODY))
    i += 1

doc = SimpleDocTemplate(
    "pdfs/Taro_Fast_Track.pdf",
    pagesize=letter,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
)
doc.build(story)
print("Done. PDF is in pdfs/Taro_Fast_Track.pdf")
PYEOF
