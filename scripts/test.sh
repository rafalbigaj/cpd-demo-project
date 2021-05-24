export PATH=$PATH:$PWD
export CPDCTL_ENABLE_CODE_PACKAGE=1

cpdctl config context use cpd_prod

qa_script_id=$QA_SCRIPT_ID
qa_code_package_id=$(<./code_package_id)
job_name="$(date +"DBScan - code package job - %Y-%m-%d_%H-%M-%S")"

read -r -d '' job_json << EOM
{
    "name": "$job_name",
    "asset_ref": "$qa_code_package_id",
    "configuration": {
        "env_id": "jupconda37oce-0127c930-fbbb-45d2-8d3b-6e38ad66a41d",
        "env_type": "notebook",
        "entrypoint": "assets/jupyterlab/scoring.py"
    }
}
EOM

echo $job_json

qa_job_id=$(cpdctl job create --space-id $qa_space_id --job '$job_json' | jq -r '.metadata.asset_id')

echo "Job ID: $job_id"

cpdctl job run create --space-id $qa_space_id --job-id $qa_job_id --job-run '{}'

cpdctl job delete --space-id $qa_space_id --job-id $qa_job_id
cpdctl code-package delete --space-id $qa_space_id --code-package-id $qa_code_package_id