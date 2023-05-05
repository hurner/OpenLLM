# Copyright 2023 BentoML Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import typing as t

import openllm
from openllm.utils import import_utils_shim as imports

_import_structure = {
    "configuration_flan_t5": ["FlanT5Config", "START_FLAN_T5_COMMAND_DOCSTRING"],
    "service_flan_t5": ["svc", "model_runner", "tokenizer_runner", "generate"],
}

try:
    if not imports.is_torch_available():
        raise openllm.exceptions.MissingDependencyError
except openllm.exceptions.MissingDependencyError:
    pass
else:
    _import_structure["modeling_flan_t5"] = ["FlanT5", "FlanT5WithTokenizer", "FlanT5Tokenizer"]

try:
    if not imports.is_flax_available():
        raise openllm.exceptions.MissingDependencyError
except openllm.exceptions.MissingDependencyError:
    pass
else:
    _import_structure["modeling_flax_flan_t5"] = ["FlaxFlanT5", "FlaxFlanT5WithTokenizer"]

try:
    if not imports.is_tf_available():
        raise openllm.exceptions.MissingDependencyError
except openllm.exceptions.MissingDependencyError:
    pass
else:
    _import_structure["modeling_flax_flan_t5"] = ["TFFlanT5", "TFFlanT5WithTokenizer"]


if t.TYPE_CHECKING:
    from .configuration_flan_t5 import \
        START_FLAN_T5_COMMAND_DOCSTRING as START_FLAN_T5_COMMAND_DOCSTRING
    from .configuration_flan_t5 import FlanT5Config as FlanT5Config

    try:
        if not imports.is_torch_available():
            raise openllm.exceptions.MissingDependencyError
    except openllm.exceptions.MissingDependencyError:
        pass
    else:
        from .modeling_flan_t5 import FlanT5 as FlanT5
        from .modeling_flan_t5 import FlanT5Tokenizer as FlanT5Tokenizer
        from .modeling_flan_t5 import \
            FlanT5WithTokenizer as FlanT5WithTokenizer

    try:
        if not imports.is_flax_available():
            raise openllm.exceptions.MissingDependencyError
    except openllm.exceptions.MissingDependencyError:
        pass
    else:
        from .modeling_flax_flan_t5 import FlaxFlanT5 as FlaxFlanT5
        from .modeling_flax_flan_t5 import \
            FlaxFlanT5WithTokenizer as FlaxFlanT5WithTokenizer

    try:
        if not imports.is_tf_available():
            raise openllm.exceptions.MissingDependencyError
    except openllm.exceptions.MissingDependencyError:
        pass
    else:
        from .modeling_tf_flan_t5 import TFFlanT5 as TFFlanT5
        from .modeling_tf_flan_t5 import \
            TFFlanT5WithTokenizer as TFFlanT5WithTokenizer
else:
    import sys

    sys.modules[__name__] = openllm.utils.LazyModule(
        __name__, globals()["__file__"], _import_structure, module_spec=__spec__
    )