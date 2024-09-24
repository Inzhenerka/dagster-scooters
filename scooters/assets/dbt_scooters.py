from dagster_dbt import DbtCliResource, dbt_assets
from dagster import file_relative_path, AssetExecutionContext, RetryPolicy, Backoff

DBT_PROJECT_DIR = file_relative_path(__file__, '../../dbt-scooters')

dbt_resource = DbtCliResource(project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROJECT_DIR)
dbt_parse_invocation = dbt_resource.cli(["parse"]).wait()
dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")


@dbt_assets(
    manifest=dbt_manifest_path,
    retry_policy=RetryPolicy(max_retries=3, delay=10, backoff=Backoff.EXPONENTIAL)
)
def dbt_models(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(['build'], context=context).stream().fetch_row_counts()
