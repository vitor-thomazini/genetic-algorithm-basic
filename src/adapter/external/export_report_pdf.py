import matplotlib
import matplotlib.pyplot as plt
import datetime as date


from domain import ExportReportProtocol

class ExportReportPDF(ExportReportProtocol):
    def __init__(self):
        matplotlib.use('PDF')

    def export(self, list):
        filename = "reports/solution_ %s" % date.datetime.now().strftime("%Y%m%d%H%M%S")

        plt.plot(list)
        plt.title("Solutions G.A.")
        plt.savefig(filename)