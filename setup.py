from setuptools import setup

# Leer dependencias desde requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='CyberiusUnzipCracker',
    version='1.0.0',
    description='Herramienta para recuperar archivos ZIP/RAR protegidos con contraseña en Windows',
    author='Cyberius Company',
    license='Proprietary',
    py_modules=['Main'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'cyberiusunzip=Main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: End Users/Desktop',
        'License :: Other/Proprietary License',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
)
