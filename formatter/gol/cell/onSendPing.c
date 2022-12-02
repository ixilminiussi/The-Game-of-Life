#include <definitions.h>
//@@//

if (!DEVICESTATE(begin))
{

    uint8_t prev = DEVICESTATE(gen) % 2;

    DEVICESTATE(gen)
    ++;

    handler_log(2, "updating and chilling");
    if (DEVICESTATE(alive) && (DEVICESTATE(liveNeighbours[prev]) == 2 || DEVICESTATE(liveNeighbours[prev]) == 3))
        DEVICESTATE(alive) = true;
    else if (!DEVICESTATE(alive) && DEVICESTATE(liveNeighbours[prev]) == 3)
        DEVICESTATE(alive) = true;
    else
        DEVICESTATE(alive) = false;

    DEVICESTATE(liveNeighbours[prev]) = 0;
    DEVICESTATE(pings[prev]) = 0;
}
else
    DEVICESTATE(begin) = 0;

MSG(alive) = DEVICESTATE(alive);
MSG(gen) = DEVICESTATE(gen);