drop procedure if exists Gett;
DELIMITER $$
CREATE PROCEDURE Gett()
BEGIN
	declare x int;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
		set x=1;
        select x;
		ROLLBACK;
    END;

    START TRANSACTION;
		insert into member (name) values ("Tony");
        insert into member (name) values ();
        insert into member (name) values ();
        insert into member (name) values ("Yahoo");
    COMMIT;
    set x=0;
    
    select x;
	
END$$

DELIMITER ;
call Gett()