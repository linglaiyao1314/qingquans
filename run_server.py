from qsapp import create_app_by_config


if __name__ == '__main__':
	myapp = create_app_by_config()
	myapp.run("0.0.0.0", port=80, debug=True)
