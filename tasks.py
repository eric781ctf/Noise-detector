from invoke import task

@task
def lint(c):
    c.run("ruff noise_detector")

@task
def format(c):
    c.run("black noise_detector")

@task
def test(c):
    c.run("pytest")

@task
def run_cli(c, duration=5):
    c.run(f"python -m noise_detector.cli --duration {duration}")

@task
def run_web(c):
    c.run("flask --app noise_detector/app.py run")