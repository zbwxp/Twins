from .ann_head import ANNHead
from .apc_head import APCHead
from .aspp_head import ASPPHead
# from .cc_head import CCHead
from .da_head import DAHead
from .dm_head import DMHead
from .dnl_head import DNLHead
from .ema_head import EMAHead
from .enc_head import EncHead
from .fcn_head import FCNHead
from .fpn_head import FPNHead
from .gc_head import GCHead
from .lraspp_head import LRASPPHead
from .nl_head import NLHead
from .ocr_head import OCRHead
# from .point_head import PointHead
# from .psa_head import PSAHead
from .psp_head import PSPHead
from .sep_aspp_head import DepthwiseSeparableASPPHead
from .sep_fcn_head import DepthwiseSeparableFCNHead
from .uper_head import UPerHead
from .bilinear_pad_head_fast_xavier_init import BilinearPADHead_fast_xavier_init

__all__ = [
    'FCNHead', 'PSPHead', 'ASPPHead',  'NLHead', 'GCHead',
    'UPerHead', 'DepthwiseSeparableASPPHead', 'ANNHead', 'DAHead', 'OCRHead',
    'EncHead', 'DepthwiseSeparableFCNHead', 'FPNHead', 'EMAHead', 'DNLHead',
    'APCHead', 'DMHead', 'LRASPPHead', 'BilinearPADHead_fast_xavier_init'
]
