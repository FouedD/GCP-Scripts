#!/bin/bash

projects=$(gcloud projects list --format='value(PROJECT_ID)')

for projectid in $projects; do
	buckets=$(gcloud storage ls --project="$projectid" 2> /dev/null)
    for bucket in $buckets; do
        gcloud storage buckets get-iam-policy $bucket | grep 'allUsers\|allAuthenticatedUsers' 1> /dev/null
        if [ $? -eq 0 ]
        then       
            echo "$projectid ---- has public bucket ------- $bucket"
            echo "----------------------"
        fi
	done
done
