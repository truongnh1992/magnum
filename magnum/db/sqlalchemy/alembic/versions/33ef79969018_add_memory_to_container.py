# Copyright 2015 Huawei Technologies Co.,LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Add memory to container

Revision ID: 33ef79969018
Revises: 2ae93c9c6191
Create Date: 2015-10-03 17:03:47.194253

"""

# revision identifiers, used by Alembic.
revision = '33ef79969018'
down_revision = '2ae93c9c6191'

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402


def upgrade():
    op.add_column('container',
                  sa.Column('memory', sa.String(length=255),
                            nullable=True))
