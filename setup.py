from setuptools import find_packages, setup

setup(
    name="scooters",
    packages=find_packages(),
    install_requires=[
        "pydantic==2.8.2",
        "dagster",
        "dagster-dbt",
        "dagster_postgres",
        "dbt-postgres",
        "dbt-core",
        "pandas",
        "matplotlib",
        "dagster-docker"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
