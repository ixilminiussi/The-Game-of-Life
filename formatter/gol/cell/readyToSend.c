#include <definitions.h>
//@@//

if (DEVICESTATE(begin))
{
    RTS(sender);
}
else if (DEVICESTATE(gen) < GRAPHPROPERTIES(end) && (DEVICESTATE(pings[DEVICESTATE(gen) % 2]) >= 8))
{
    if (DEVICESTATE(gen) % GRAPHPROPERTIES(cycles) == 0)
        RTSSUP();
    RTS(sender);
}