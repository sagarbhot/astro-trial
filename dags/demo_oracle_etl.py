"""
demo_oracle_etl
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from airflow.providers.amazon.aws.operators.eks import EksPodOperator
from airflow.providers.oracle.operators.oracle import OracleStoredProcedureOperator
import pendulum


@dag(
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2023-08-04", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
)
def demo_oracle_etl():
    oracle_stored_procedure_operator_1 = OracleStoredProcedureOperator(
        procedure="oracle_sp_task",
        oracle_conn_id="my_oracle_connection",
        task_id="oracle_stored_procedure_operator_1",
    )

    eks_pod_operator_1 = EksPodOperator(
        kubernetes_conn_id="my_aws_connection",
        cluster_name="fr_cluster",
        task_id="eks_pod_operator_1",
    )

    eks_pod_operator_1 << oracle_stored_procedure_operator_1

dag_obj = demo_oracle_etl()
