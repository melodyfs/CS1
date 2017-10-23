import random, sys
# Predictable random numbers, but help with testing
random.seed(42)
from person import Person
import pdb
# from logger import Logger

class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.

    _____Attributes______

    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.

    population_size: Int.  The size of the population for this simulation.

    population: [Person].  A list of person objects representing all people in
        the population.

    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.

    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.

    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.

    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.

    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.


    _____Methods_____

    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.

    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.population = {}
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = {}
        self.newly_infected = []

        self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        infected_count = 0

        while len(population) != self.population_size:
            if infected_count !=  initial_infected:
                infected_person = Person(self.next_person_id, False, self.virus_name)
                population.append(infected_person)
                self.next_person_id += 1
                infected_count += 1
            else:
                new_person = Person(self.next_person_id, False, None)
                random_num = random.randint(0,1)
                if random_num < self.vacc_percentage:
                    self.next_person_id += 1
                    new_person.is_vaccinated = True
                    population.append(new_person)
                else:
                    population.append(new_person)
                    self.next_person_id += 1
                    self.newly_infected.append(new_person)
            self.next_person_id += 1

        self.population = population

        for person in population:
            print("id:{}\tV:{}\tI:{}".format(person._id, person.is_vaccinated,
            person.infected))

        return population


    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive is True:
                return True


    def run(self):
        time_step_counter = 0
        self._simulation_should_continue()
        should_continue = None
        while should_continue:
            self.time_step()
            self._simulation_should_continue()
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        time_step = 0

        for person in self.newly_infected:
            while time_step != 100:
                random_num = random.randint(0, 100)
                random_person = self.population[random_num]
                if random_person.is_alive is False:
                    another_person = self.population[random_num]
                    print("Grab %s" % another_person)


    def interaction(self, person, random_person):
        # Person1 is infected
        assert person1.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated is True:
            self.logger.log_interaction(person1, random_person, person2_vacc=True)
        elif random_person.infected is not None:
            self.logger.log_interaction(person1, random_person, did_infect=True)
        elif person1.infected is None and random_person.is_vaccinated is not False:
            random_num = random.randint(0, 1)
            if random_num < self.basic_repro_num:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person1, random_person, did_infect=True)


    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infected = True
        self.newly_infected = []

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)

    simulation.run()

# simulation = Simulation(10, 0.7, "Mers", 0.45, 0.6, 3)
# simulation._create_population(3)
# simulation.time_step()
