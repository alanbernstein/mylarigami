from flask import Flask, render_template, request, Response, send_file
import io

app = Flask(__name__)

# SVG Generator function
def test_generate(color="black", size=100):
    svg_template = f'''
    <svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
        <circle cx="{size // 2}" cy="{size // 2}" r="{size // 3}" fill="{color}" />
    </svg>
    '''
    return svg_template

def mylar_crease_test_generate(size=100):
    svg_template = '''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <!-- Square path in black -->
        <path d="M 50 50 L 150 50 L 150 150 L 50 150 Z" stroke="black" fill="none" stroke-width="2" />
        <!-- Diagonals in red -->
        <path d="M 50 50 L 150 150" stroke="red" stroke-width="2" />
        <path d="M 50 150 L 150 50" stroke="red" stroke-width="2" />
    </svg>
    '''
    return svg_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

# Route to generate the SVG and return as text for preview
@app.route('/test/preview', methods=['POST', "GET"])
def test_preview():
    color = request.form.get('color', 'black')
    size = int(request.form.get('size', 100))
    svg_data = test_generate(color=color, size=size)
    return svg_data, 200, {'Content-Type': 'image/svg+xml'}

# Route to download the generated SVG
@app.route('/test/download', methods=['POST'])
def test_download():
    color = request.form.get('color', 'black')
    size = int(request.form.get('size', 100))
    svg_data = test_generate(color=color, size=size)
    svg_bytes = io.BytesIO(svg_data.encode('utf-8'))
    return send_file(svg_bytes, mimetype='image/svg+xml', as_attachment=True, download_name='test.svg')

@app.route('/mylar/crease-test')
def mylar_crease_test():
    return render_template('mylar-crease-test.html')

# Route to generate the SVG and return as text for preview
@app.route('/mylar/crease-test/preview', methods=['POST'])
def mylar_crease_test_preview():
    size = int(request.form.get('size', 100))
    svg_data = mylar_crease_test_generate(size=size)
    return svg_data, 200, {'Content-Type': 'image/svg+xml'}

# Route to download the generated SVG
@app.route('/mylar/crease-test/download', methods=['POST'])
def mylar_crease_test_download():
    size = int(request.form.get('size', 100))
    svg_data = mylar_crease_test_generate(size=size)
    svg_bytes = io.BytesIO(svg_data.encode('utf-8'))
    return send_file(svg_bytes, mimetype='image/svg+xml', as_attachment=True, download_name='mylar-crease-test.svg')


if __name__ == '__main__':
    app.run(debug=True)
