# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from abc import ABC, abstractmethod

from syne_tune.optimizer.schedulers.searchers.bayesopt.datatypes.common import (
    Configuration,
)
from syne_tune.optimizer.schedulers.searchers.bayesopt.tuning_algorithms.common import (
    ExclusionList,
)


class DuplicateDetector(ABC):
    @abstractmethod
    def contains(
        self, existing_candidates: ExclusionList, new_candidate: Configuration
    ) -> bool:
        pass


class DuplicateDetectorNoDetection(DuplicateDetector):
    def contains(
        self, existing_candidates: ExclusionList, new_candidate: Configuration
    ) -> bool:
        return False  # no duplicate detection at all


class DuplicateDetectorIdentical(DuplicateDetector):
    def contains(
        self, existing_candidates: ExclusionList, new_candidate: Configuration
    ) -> bool:
        return existing_candidates.contains(new_candidate)
