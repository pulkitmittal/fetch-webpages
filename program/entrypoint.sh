#!/usr/bin/env bash

set -o errexit
set -o pipefail

__dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
gosu appuser python $__dir/main.py "$@"
