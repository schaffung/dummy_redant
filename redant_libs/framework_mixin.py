from redant_libs.ops_libs.peer_ops import peer_ops
from redant_libs.support_libs.rexe import Remote_ops
from redant_libs.ops_libs.volume_ops import volume_ops

class frameworkMixin(Remote_ops, peer_ops, volume_ops):
    pass
