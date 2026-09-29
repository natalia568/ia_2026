from aspirador import joc_gui
from aspirador import agent


agents = [agent.AspiradorTaula()]

hab = joc_gui.Aspirador(agents)
hab.comencar()