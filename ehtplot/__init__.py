# Copyright (C) 2017--2019 Lia Medeiros & Chi-kwan Chan
# Copyright (C) 2017--2019 Steward Observatory
#
# This file is part of ehtplot.
#
# ehtplot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ehtplot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ehtplot.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

# Register default colormaps and themes in packages
from .color  import *
from .theme  import *

# ehtplot Objects
from .panel  import *
from .figure import *
from .visual import *

# ehtplot API
from .api    import *
