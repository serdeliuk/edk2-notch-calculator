#!/usr/bin/env python2.7

###############################################################################################################################
#
# EDK2 framebuffer addresses calculator
# Provides addresses to exclude from the video frame buffer rounded corners and camera space by creating a header and a footer
#
# By Marc Serdeliuk, 2022 https://github.com/serdeliuk/edk2-notch-calculator
#
###############################################################################################################################

#token name
SpaceGuid="Pad5Pkg";

# Font Sie is specified in Include/Resources/font5x12.h
FontHorizontalSize=5;
FontVerticalSize=12;

# How many text line header/footer should have? ---- assuming are equal
HeaderVerticalTextLines=5;

# From UEFIPLAT Display Reserved MemBase
FrameBufferStart="0x9C000000";

# Obtained with adb shell wm size
HorizontalSize=1600;
VerticalSize=2560;

# bytes per pixel
BytesPerPixel=32;

###############################################################################################################################
#
# USUALLY AFTER THIS LINE YOU DO NOT NEED TO EDIT ANY VALUES
#
###############################################################################################################################

# Full Srceen size in pixels plus attributes
FullScreenSize=HorizontalSize*VerticalSize*(BytesPerPixel/8);

# Header size in pixels plus attributes
HeaderSize=((HeaderVerticalTextLines*FontVerticalSize)*(BytesPerPixel/8)*HorizontalSize);

print("\nPlease add to your DSC file %s.dsc the following lines in [PcdsFixedAtBuild.common] section:" % (SpaceGuid));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferHeaderAddress|0x%X" % (SpaceGuid, int(FrameBufferStart,16)));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferAddress|0x%X" % (SpaceGuid, int(FrameBufferStart,16)+HeaderSize));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferFooterAddress|0x%X" % (SpaceGuid, (int(FrameBufferStart,16)+HeaderSize)+(FullScreenSize-HeaderSize*2)));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferWidth|%d" % (SpaceGuid, HorizontalSize));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferHeight|%d\n" % (SpaceGuid, VerticalSize-(HeaderVerticalTextLines*FontVerticalSize*2)));


print("\nPlease add to your DEC file %s.dec the following lines in [PcdsFixedAtBuild.common] section:" % (SpaceGuid));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferAddress|0x%X|UINT32|0x0000a400" % (SpaceGuid, int(FrameBufferStart,16)));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferHeaderAddress|0x%X|UINT32|0x0000a401" % (SpaceGuid, int(FrameBufferStart,16)));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferFooterAddress|0x%X|UINT32|0x0000a402" % (SpaceGuid, int(FrameBufferStart,16)));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferWidth|%d|UINT32|0x0000a403" % (SpaceGuid, HorizontalSize));
print("\tg%sTokenSpaceGuid.PcdMipiFrameBufferHeight|%d|UINT32|0x0000a404" % (SpaceGuid, VerticalSize));
