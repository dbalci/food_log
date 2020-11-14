#!/bin/bash

rm test.db

source env/bin/activate
python3 << EOF
from app import db
db.create_all()
EOF

