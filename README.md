DI KiCad Library
================
This library contains KiCad symbols, footprints, and 3d models I use for my
projects.

packages3d
===========
This directory contains 3D models for various components.

Battery.3dshapes/BatteryHolder_LINX_BAT-HLD-001
-----------------------------------------------
Model of the LINX BAT-HLD_001.

**WARNING:** This is only a rough model. Dimensions are not 100% accurate and
curve at the front side is missing.

Button_Switch_SMD.3dshapes/SW_SPST_eBay_261995936109
----------------------------------------------------
Model of a surface mounted tactile push butotn I bought on eBay as item
Number 261995936109 in April 2017. I don't know if the buttons currently sold
as this item are the same. The image looks different from the buttons I have.

Connector_Molex.3dshapes/Molex_PicoBlade_53048
----------------------------------------------
These are models for the Molex PicoBlade 53048 series of connectors.

The FreeCAD model is parameterized, allowing one model to be used for the
various pin counts. The pin count can be changed in the 'propertySheet'.

But be carefull sometimes the solver gets confused if you change the
parameters. So always check if the model is still okay. Also after exporting
with KicadStepUp the model is broken, and has to be reverted.

**NOTE:** The indentations on the rear top edge are missing.
