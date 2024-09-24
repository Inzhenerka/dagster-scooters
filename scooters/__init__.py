from dagster import Definitions, load_assets_from_modules
from .assets import dbt_scooters

defs = Definitions(
        assets=load_assets_from_modules([dbt_scooters]),
        resources={
            'dbt': dbt_scooters.dbt_resource
        }
)
