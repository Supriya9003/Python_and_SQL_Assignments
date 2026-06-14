 create table joints(joint_id int primary key,
                                      -> join_name varchar(50),
                                      -> bone1_id int,
                                      -> bone2_id int,
                                      -> joint_type_id int,
                                      -> details text,
                                      -> foreign key(bone1_id) references bones(bone_id),
                                      -> foreign key(bone2_id) references bones(bone_id),
                                      -> foreign key(joint_type_id) references jointtypes(joint_type_id));



 insert into bones values(1,'Humerus', 'Upper arm bone'),
                                      '> (2,'Ulna', 'Forearm bone'),
                                      '> (3,'Scapula', 'Shoulder blade'),
                                      '> (4, 'Femur', 'Thigh bone'),(5, 'Pelvis', 'Hip bone'),
                                      '> (6, 'Radius', 'Forearm bone');


 insert into joints values(1, 'Elbow', 1,2,1,'Hinge joint of the arm'),
                                      -> (2, 'Shoulder', 1,3,2, 'Ball-and-socket joint'),
                                      -> (3, 'Hip', 4,5,2, 'Ball-and-socket joint of the hip'),
                                      -> (4, 'Proximal Radioulnar', 6,2,1, 'Pivot-like hinge movement'),
                                      -> (5,'Humeroradial', 1,6,1, 'Part of the elbow complex');

 select * from joints;


select * from bones;


 select * from jointtypes;


 alter table joints change join_name joint_name varchar(50);


 describe jointtypes;


select j.joint_name from joints j join jointtypes jt on j.joint_type_id = jt.joint_type_id where jt.bone_name = 'Hinge';



select b1.bone_name as Bone_A, b2.bone_name as Bone_B from joints j join Bones b1 on j.bone1_id=b1.bone_id join Bones b2 on j.bone2_id=b2.bone_id where j.joint_name = 'Elbow';
+---------+--------+
| Bone_A  | Bone_B |
+---------+--------+
| Humerus | Ulna   |
+---------+--------+
