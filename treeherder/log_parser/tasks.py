# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.


import logging

from celery import task

from treeherder.log_parser.utils import (extract_log_artifacts,
                                         extract_struct_log_artifacts,
                                         post_log_artifacts
                                         )

logger = logging.getLogger(__name__)


@task(name='parse-log', max_retries=10)
def parse_log(project, job_log_url, job_guid, check_errors=False):
    """
    Call ArtifactBuilderCollection on the given job.
    """

    # if parse_status is not available, consider it pending
    parse_status = job_log_url.get("parse_status", "pending")
    # don't parse a log if it's already been parsed
    if parse_status == "parsed":
        return

    post_log_artifacts(project,
                       job_guid,
                       job_log_url,
                       parse_log,
                       extract_log_artifacts,
                       check_errors
                       )


@task(name='parse-struct-log', max_retries=10)
def parse_struct_log(project, job_log_url, job_guid, check_errors=False):
    """
    Apply the Structured Log Fault Formatter to the structured log for a job.
    """
    post_log_artifacts(project,
                       job_guid,
                       job_log_url,
                       parse_struct_log,
                       extract_struct_log_artifacts,
                       check_errors
                       )
