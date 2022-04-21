# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""
`circuitpython_typing.pwmio`
================================================================================

Type annotation definitions for PWMOut where Blinka doesn't otherwise define it.

* Author(s): Alec Delaney
"""

# # Protocol was introduced in Python 3.8.
try:
    from typing import Union, Tuple, Protocol
except ImportError:
    from typing_extensions import Protocol

class PWMOut(Protocol):
    """Protocol that implements, at the bare minimum, the `duty_cycle` property"""

    @property
    def duty_cycle(self) -> int:
        """The duty cycle as a ratio using 16-bits"""
        ...

    @duty_cycle.setter
    def duty_cycle(self, duty_cycle: int) -> None:
        ...
