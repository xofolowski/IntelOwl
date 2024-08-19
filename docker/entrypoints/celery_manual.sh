#!/bin/bash

until cd /opt/deploy/intel_owl
do
    echo "Waiting for server volume..."
done

# Apply database migrations
echo "Waiting for db and UWSGI to be ready..."
sleep 10

echo "environment: $STAGE"
if [ $STAGE = "local" ]
then
   worker_number=4
elif [ $STAGE = "staging" ]
then
   worker_number=4
elif [ "$STAGE" = "ci" ]
then
  worker_number=1
else
   # default is prod
   worker_number=4
fi

echo "worker number: $worker_number"

ARGUMENTS="-A intel_owl.celery worker -n worker_local --uid www-data --time-limit=10000 --gid www-data --pidfile= -c $worker_number -Ofair -Q local_manual.fifo,long_manual.fifo,default_manual.fifo -E --without-gossip"
if [[ $DEBUG == "True" ]] && [[ $DJANGO_TEST_SERVER == "True" ]];
then
    echo "Running celery with autoreload"
    python3 manage.py celery_reload -c "$ARGUMENTS"
else
  /usr/local/bin/celery $ARGUMENTS
fi