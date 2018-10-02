from Experiment import Experiment

def main():
    experiment = Experiment()
    experiment.gatherResults()
    experiment.plotHist(experiment.results)
main()
