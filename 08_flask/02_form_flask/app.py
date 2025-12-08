from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML do formulário como template string
html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário Flask</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2rem; }
        form { max-width: 400px; padding: 1rem; border: 1px solid #ccc; border-radius: 8px; }
        label { font-weight: bold; }
        input { width: 100%; padding: 0.5rem; margin-top: 0.25rem; margin-bottom: 1rem; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 0.5rem 1rem; background-color: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        h2 { color: green; }
    </style>
</head>
<body>
    <main>
        <h1>Formulário</h1>
        <hr>
        <form method="POST">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" placeholder="Digite seu nome" required>
            <button type="submit">Enviar</button>
        </form>

        {% if nome %}
            <h2>Olá, {{ nome }}!</h2>
        {% endif %}
    </main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def enviar():
    nome = None
    if request.method == "POST":
        nome = request.form.get("nome")  # pega o valor correto do input
    return render_template_string(html_template, nome=nome)

if __name__ == "__main__":
    app.run(debug=True)
