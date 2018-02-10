class PeakFinder:
    @staticmethod
    def one_dimension(inputlist):
        inlen = len(inputlist)
        if inlen < 2:
            return inputlist

        peaks = []

        if inputlist[0] > inputlist[1]:
            peaks.append(inputlist[0])

        for i in range(1, inlen - 2):
            if inputlist[i] > inputlist[i - 1] and inputlist[i] > inputlist[i + 1]:
                peaks.append(inputlist[i])

        if inputlist[inlen - 1] > inputlist[inlen - 2]:
            peaks.append(inputlist[inlen - 1])

        return peaks
