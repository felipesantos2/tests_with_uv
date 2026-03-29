from flask import Flask, request
from markupsafe import escape

from werkzeug import utils

app = Flask(__name__)

# <script> alert('Olá') <\/script>
# escape is required!!!! danger

providers: list = [
	'blank',
	'RKM',
	'Pastelaria Central',
	'Xereta Supermercados',
	'Pastelaria Central',
	'Compre Bem',
	'Banco do Brasil',
	'Leterias Caixa',
	'Farmacia Indiana',
]


@app.route('/')
def home() -> str:
	return utils.redirect(location, code=302, Response=None)


@app.route('/providers')
def all_providers() -> str:
	name: str = request.args.get('name', 'Flask')

	return f"""

		<h1 style="font-family: Arial;">Providers</h1>

			<ul>
				<li>
					{escape(name)}
				</li>

				<li>
					RKM
				</li>

				<li>
					Pastelaria Central
				</li>
			</ul>
		"""


@app.route('/providers/<int:provider>/provider')
def show_provider(provider: int) -> str:

	if len(providers) >= provider:
		if provider == 0:
			return providers[1]
		#early return
		return providers[provider]
	else:
		return providers[1]


if __name__ == '__main__':
	app.run(debug=True)
