@load custom-scripts/custom-notices

event bro_init() {
        NOTICE([$note=CustomNotice::Bro_Start,
        $msg = "Bro engine started!"]);
}
event new_connection(c: connection) {
        if (c$id$resp_h != 0.0.0.0) {
                NOTICE([$note=CustomNotice::Bing_User_Detected,
                $msg = fmt("Bing user detect: %s", c$id$orig_h)]);
        }
}
event bro_done() {
        NOTICE([$note=CustomNotice::Bro_Stop,
        $msg = "Bro engine stopped!"]);
}
