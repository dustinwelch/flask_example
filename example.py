from flask import Flask, render_template


app = Flask(__name__)

@app.route('/index')
def index():
	return '''
		<head>
	<title>Example</title>
</head>

<style>
	.button{
		color: #000;
		float: left;
		font-size: 28px;
		font-weight: bold;
		}
</style>

<body>
<div class="container bg-secondary">
	<h1 id='text'>Here's my example</h1>
	<button id='change'onClick=change_text()>Click to Change Text</button>
</div>
</body>



<script>
function change_text(){	
	document.getElementById('text').innerHTML = 'changed'
	}
</script>
	
	'''

