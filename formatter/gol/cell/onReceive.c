#include <definitions.h>
//@@//

DEVICESTATE(pings[MSG(gen) % 2]) ++;
DEVICESTATE(liveNeighbours[MSG(gen) % 2]) += MSG(alive);