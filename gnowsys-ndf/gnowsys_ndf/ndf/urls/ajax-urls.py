from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from gnowsys_ndf.ndf.views import ajax_views

urlpatterns = patterns('gnowsys_ndf.ndf.views.ajax_views',
    url(r'^collection/', 'select_drawer', name='select_drawer'),
    url(r'^collectionNav/', 'collection_nav', name='collection_nav'),
    url(r'^collectionView/', 'collection_view', name='collection_view'),
    url(r'^shelf/', 'shelf', name='shelf'),
    url(r'^add_subThemes/', 'add_sub_themes', name='add_sub_themes'),
    url(r'^add_ThemeItems', 'add_theme_item', name='add_theme_item'),
    url(r'^add_page/', 'add_page', name='add_page'),
    url(r'^add_files/', 'add_file', name='add_file'),
    url(r'^deleteThemes/', 'delete_themes', name='delete_themes'),
    url(r'^add_Topics/', 'add_topics', name='add_topics'),
    url(r'^Collection_create/', 'collection_create', name='collection_create'),
    url(r'^get_tree_hierarchy/(?P<node_id>[\w-]+)$', 'get_tree_hierarchy', name='get_tree_hierarchy'),
    url(r'^get_collection/(?P<node_id>[\w-]+)$', 'get_collection', name='get_collection'),
    url(r'^get_collection/(?P<node_id>[\w-]+)/(?P<no_res>[\w-]+)$', 'get_collection', name='get_course_collection'),
    url(r'^get_contents/', 'get_topic_contents', name='get_topic_contents'),
    url(r'^drawer/', 'drawer_widget', name='drawer_widget'),
    url(r'^search/', 'search_drawer', name='search_drawer'),
    url(r'^terms/', 'terms_list', name='terms_list'),
    url(r'^change_group_settings/', 'change_group_settings', name='change_group_settings'),
    url(r'^make_module/', 'make_module_set', name='make_module'),
    url(r'^get_module_json/', 'get_module_json', name='get_module_json'),
    url(r'^get_graph_json/', 'graph_nodes', name='get_graph_json'),
    url(r'^get_data_for_drawer/', 'get_data_for_drawer', name='get_data_for_drawer'),
    url(r'^get_data_for_drawer_of_attributetype_set/', 'get_data_for_drawer_of_attributetype_set', name='get_data_for_drawer_of_attributetype_set'),
    url(r'^get_data_for_drawer_of_relationtype_set/', 'get_data_for_drawer_of_relationtype_set', name='get_data_for_drawer_of_relationtype_set'),
    url(r'^deletionInstances/', 'deletion_instances', name='deletion_instances'),
    url(r'^get_visited_location/', 'get_visited_location', name='get_visited_location'),
    # url(r'^get_online_editing_user/', 'get_online_editing_user', name="get_online_editing_user"),
    url(r'^view_articles/', 'view_articles', name="view_articles"),
    url(r'^get_author_set_users/', 'get_author_set_users', name="get_author_set_users"),
    url(r'^get_filterd_user_list/', 'get_filterd_user_list', name="get_filterd_user_list"),
    url(r'^search_tasks/', 'search_tasks', name="search_tasks"),
    url(r'^get_group_member_user/', 'get_group_member_user', name="get_group_member_user"),
    url(r'^remove_user_from_author_set/', 'remove_user_from_author_set', name="remove_user_from_author_set"),
    url(r'^get_data_for_user_drawer/', 'get_data_for_user_drawer', name='get_data_for_user_drawer'),
    url(r'^get_data_for_batch_drawer/', 'get_data_for_batch_drawer', name='get_data_for_batch_drawer'),
    url(r'^get_resource_by_oid_list$', 'get_resource_by_oid_list', name='get_resource_by_oid_list'),
    url(r'^get_resource_by_oid/?', 'get_resource_by_oid', name='get_resource_by_oid'),
    url(r'^get_ckeditor/?', 'get_ckeditor', name='get_ckeditor'),
    url(r'^get_gin_line_template/(?P<node_id>[\w-]+)$', 'get_gin_line_template', name='get_gin_line_template'),
    url(r'^course_create_collection/', 'course_create_collection', name='course_create_collection'),
    url(r'^course_create_note/', 'course_create_note', name='course_create_note'),#create note in gallery and raw material
    url(r'^upload_file_ckeditor', 'upload_file_ckeditor', name='upload_file_ckeditor'),
    url(r'^upload_video_thumbnail', 'upload_video_thumbnail', name='upload_video_thumbnail'),
    # url(r'^upload_ost_files', 'upload_ost_files', name='upload_ost_files'),
    url(r'^get_video_player', 'get_video_player', name='get_video_player'),
    url(r'^get_audio_player', 'get_audio_player', name='get_audio_player'),
    url(r'^get_jhapps', 'get_jhapps', name='get_jhapps'),
    url(r'^create_edit_asset', 'create_edit_asset', name='create_edit_asset'),
    url(r'^add_assetcontent', 'add_assetcontent', name='add_assetcontent'),
    url(r'^add_asset', 'add_asset', name='add_asset'),
    url(r'^delete_asset', 'delete_asset', name='delete_asset'),
    url(r'^get_metadata_page', 'get_metadata_page', name='get_metadata_page'),
    url(r'^get_interaction_widget', 'get_interaction_widget', name='get_interaction_widget'),
    url(r'^save_metadata', 'save_metadata', name='save_metadata'),
    url(r'^save_interactions', 'save_interactions', name='save_interactions'),
    url(r'^export_to_epub/(?P<node_id>[\w-]+)', 'export_to_epub', name='export_to_epub'),
    url(r'^remove_related_oc/', 'remove_related_doc', name='remove_related_doc'),
    url(r'^get_admin_page_form', 'get_admin_page_form', name='get_admin_page_form'),
    url(r'^get_help_page_form', 'get_help_page_form', name='get_help_page_form'),
    
    # url(r'^/upload_file/', 'upload_file', name='upload_file'),

                       # Ajax-urls required for MIS --------------------------------

    url(r'^get_detailed_report/', 'get_detailed_report', name='get_detailed_report'),
    url(r'^get_universities/', 'get_universities', name='get_universities'),
    url(r'^get_students_for_batches/', 'get_students_for_batches', name='get_students_for_batches'),
    url(r'^get_anncourses_allstudents/', 'get_anncourses_allstudents', name='get_anncourses_allstudents'),
    url(r'^get_courses/', 'get_courses', name='get_courses'),
    url(r'^get_batches_with_acourse/', 'get_batches_with_acourse', name='get_batches_with_acourse'),
    url(r'^get_announced_courses_with_ctype/', 'get_announced_courses_with_ctype', name='get_announced_courses_with_ctype'),
    url(r'^get_colleges/(?P<app_id>[\w-]+)$', 'get_colleges', name='get_colleges'),
    url(r'^get_districts/', 'get_districts', name='get_districts'),
    url(r'^get_affiliated_colleges/', 'get_affiliated_colleges', name='get_affiliated_colleges'),
    url(r'^get_students/', 'get_students', name='get_students'),
    url(r'^get_students_for_approval/', 'get_students_for_approval', name='get_students_for_approval'),
    url(r'^approve_students/', 'approve_students', name='approve_students'),
    url(r'^get_statewise_data/', 'get_statewise_data', name='get_statewise_data'),
    url(r'^get_college_wise_students_data/', 'get_college_wise_students_data', name='get_college_wise_students_data'),
    url(r'^rechedule_event/(?P<node>[\w-]+)$','reschedule_task',name='reschedule_task'),
    url(r'^set_user_link/', 'set_user_link', name='set_user_link'),
    url(r'^set_enrollment_code/', 'set_enrollment_code', name='set_enrollment_code'),
    url(r'^get_students_assignments/', 'get_students_assignments', name='get_students_assignments'),
    url(r'^get_course_details_for_trainer/', 'get_course_details_for_trainer', name='get_course_details_for_trainer'),
    url(r'^event_assginee/(?P<app_set_instance_id>[\w-]+)$', 'event_assginee', name='event_assginee'),
    url(r'^save_csv/(?P<app_set_instance_id>[\w-]+)$', 'save_csv', name='save_csv'),
    url(r'^assessment/(?P<app_set_instance_id>[\w-]+)$','get_assessment',name='get_assessment'),
    url(r'^edit_task_title/', 'edit_task_title', name='edit_task_title'),
    url(r'^get_attendees/(?P<node>[\w-]+)$', 'get_attendees', name='get_attendees'),
    url(r'^attendees/(?P<node>[\w-]+)$', 'get_attendance', name='get_attendance'),
    url(r'^attendees_relations/(?P<node>[\w-]+)$', 'attendees_relations', name='attendees_relations'),
    url(r'^close_event/(?P<node>[\w-]+)$', 'close_event', name='close_event'),
    url(r'^fetch_course_name/(?P<Course_type>[^/]+)$', 'fetch_course_name', name='fetch_course_name'),
    url(r'^fetch_course_Module/(?P<announced_course>[^/]+)$', 'fetch_course_Module', name='fetch_course_Module'),
    url(r'^fetch_course_session/(?P<Course_name>[^/]+)$', 'fetch_course_session', name='fetch_course_session'),
    url(r'^fetch_course_batches/(?P<Course_name>[^/]+)$', 'fetch_course_batches', name='fetch_course_batches'),
    url(r'^fetch_batch_student/(?P<Course_name>[^/]+)$', 'fetch_batch_student', name='fetch_batch_student'),
    url(r'^events/', 'get_data_for_event_task', name='get_data_for_event_task'),
    url(r'^edit_task_content/', 'edit_task_content', name='edit_task_content'),
    url(r'^insert_picture/', 'insert_picture', name="insert_picture"),
    #url for infinite scroll down
    url(r'^page_scroll/(?P<page>[^/]+)$', 'page_scroll', name='page_scroll'),
    url(r'^check_date/(?P<node>[\w-]+)$', 'check_date', name='check_date'),
    url(r'^save_time/(?P<node>[\w-]+)$', 'save_time', name='save_time'),
    url(r'^show_coll_cards/$', 'show_coll_cards', name='show_coll_cards'),
    url(r'^get_visits_count/$', 'get_visits_count', name='get_visits_count'),
    url(r'^search_users/$', 'search_users', name='search_users'),
    url(r'^save_user_password/$', 'save_user_password', name='save_user_password'),
    url(r'^get_paged_images/', 'get_paged_images', name='get_paged_images'),
    url(r'^get_templates_page/', 'get_templates_page', name='get_templates_page'),
    url(r'^get_group_templates_page/', 'get_group_templates_page', name='get_group_templates_page'),
    url(r'^add_transcript/', 'add_transcript', name='add_transcript'),
    url(r'^get_node_json_from_id/', 'get_node_json_from_id', name='get_node_json_from_id'),
    url(r'^save_node/', 'save_node', name='save_node'),
    url(r'^get_group_pages/$', 'get_group_pages', name='get_group_pages'),
    url(r'^get_info_pages/$', 'get_info_pages', name='get_info_pages'),
    url(r'^add_to_collection_set/$', 'add_to_collection_set', name='add_to_collection_set'),
    url(r'^remove_from_nodelist/$', 'remove_from_nodelist', name='remove_from_nodelist'),
    url(r'^ajax_delete_node/$', 'ajax_delete_node', name='ajax_delete_node'),
    url(r'^get_translated_node/$', 'get_translated_node', name='get_translated_node'),

    # url for graph display
    url(r'^graph/adminRenderGraph/(?P<node_id>[^/]+)/fetch/(?P<graph_type>[^/]+)$', 'adminRenderGraph', name='adminRenderGraph'),
    url(r'^get_rating_template/$', 'get_rating_template', name='get_rating_template'),

)