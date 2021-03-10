import inspect
import importlib
from redant_libs.framework_mixin import frameworkMixin

object_val = frameworkMixin(12)

module_name = "test_sample_tc.py".strip(".py")
module = importlib.import_module(module_name)
test_class_str = inspect.getmembers(module, inspect.isclass)[0][0]

test_class = getattr(module, test_class_str)
test_object = test_class(object_val)
test_func = getattr(test_object, "test_fn")
test_func()

