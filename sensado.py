#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Sensado
# Generated: Sun Nov 24 15:11:16 2013
##################################################

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class sensado(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Sensado")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.umbral = umbral = 0
        self.samp_rate = samp_rate = 44000
        self.fc = fc = 0

        ##################################################
        # Blocks
        ##################################################
        self.usando_power_squelch = analog.pwr_squelch_cc(umbral, 1, 100, False)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.sensado_primario = analog.probe_avg_mag_sqrd_c(0, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.usando_power_squelch, 0), (self.sensado_primario, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.usando_power_squelch, 0))


# QT sink close method reimplementation

    def get_umbral(self):
        return self.umbral

    def set_umbral(self, umbral):
        self.umbral = umbral
        self.usando_power_squelch.set_threshold(self.umbral)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_source_0.set_center_freq(self.fc, 0)
