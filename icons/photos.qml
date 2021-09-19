<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" simplifyAlgorithm="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" labelsEnabled="0" simplifyDrawingHints="0" readOnly="0" maxScale="0" simplifyDrawingTol="1" version="3.16.4-Hannover" hasScaleBasedVisibilityFlag="0" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal endField="" mode="0" enabled="0" startExpression="" accumulate="0" fixedDuration="0" durationUnit="min" startField="" durationField="" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="RuleRenderer">
    <rules key="{eda3b88d-53d7-449e-a3fd-8bb24f0f1962}">
      <rule key="{3f4b774f-8e6f-494d-86e0-0c50d8ea78da}" symbol="0"/>
    </rules>
    <symbols>
      <symbol force_rhr="0" alpha="1" name="0" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0.00000000000000006,-10" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="5.4" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="if( &quot;AZIMUTH&quot; !=0,5.4,0)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="97,97,97,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="14" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="-2,1" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="5" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="2,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="7" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="-1,-3" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if( &quot;AZIMUTH&quot; !=0,2,0)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="QFieldSync/action" value="no_action"/>
    <property key="QFieldSync/photo_naming" value="{&quot;Path&quot;: &quot;'DCIM/test-1_' || format_date(now(),'yyyyMMddhhmmsszzz') || '.jpg'&quot;}"/>
    <property key="dualview/previewExpressions">
      <value>"Name"</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory spacingUnitScale="3x:0,0,0,0,0,0" diagramOrientation="Up" sizeType="MM" rotationOffset="270" penWidth="0" maxScaleDenominator="1e+08" scaleDependency="Area" barWidth="5" spacing="5" spacingUnit="MM" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" labelPlacementMethod="XHeight" height="15" penColor="#000000" backgroundAlpha="255" minimumSize="0" enabled="0" showAxis="1" width="15" backgroundColor="#ffffff" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" penAlpha="255" direction="0" opacity="1" minScaleDenominator="0">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <axisSymbol>
        <symbol force_rhr="0" alpha="1" name="" clip_to_extent="1" type="line">
          <layer class="SimpleLine" enabled="1" locked="0" pass="0">
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" priority="0" dist="0" obstacle="0" placement="0" zIndex="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="ID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Date">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Time">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Lon">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Lat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Altitude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="North">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Azimuth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Cam. Maker">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Cam. Model">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Title">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Comment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Path">
      <editWidget type="ExternalResource">
        <config>
          <Option type="Map">
            <Option name="DocumentViewer" value="1" type="int"/>
            <Option name="DocumentViewerHeight" value="250" type="int"/>
            <Option name="DocumentViewerWidth" value="350" type="int"/>
            <Option name="FileWidget" value="true" type="bool"/>
            <Option name="FileWidgetButton" value="true" type="bool"/>
            <Option name="FileWidgetFilter" value="" type="QString"/>
            <Option name="PropertyCollection" type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
            <Option name="RelativeStorage" value="0" type="int"/>
            <Option name="StorageMode" value="0" type="int"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="RelPath">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Timestamp">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Images">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="fid"/>
    <alias index="1" name="" field="ID"/>
    <alias index="2" name="" field="Name"/>
    <alias index="3" name="" field="Date"/>
    <alias index="4" name="" field="Time"/>
    <alias index="5" name="" field="Lon"/>
    <alias index="6" name="" field="Lat"/>
    <alias index="7" name="" field="Altitude"/>
    <alias index="8" name="" field="North"/>
    <alias index="9" name="" field="Azimuth"/>
    <alias index="10" name="" field="Cam. Maker"/>
    <alias index="11" name="" field="Cam. Model"/>
    <alias index="12" name="" field="Title"/>
    <alias index="13" name="" field="Comment"/>
    <alias index="14" name="" field="Path"/>
    <alias index="15" name="" field="RelPath"/>
    <alias index="16" name="" field="Timestamp"/>
    <alias index="17" name="" field="Images"/>
  </aliases>
  <defaults>
    <default expression="" applyOnUpdate="0" field="fid"/>
    <default expression="" applyOnUpdate="0" field="ID"/>
    <default expression="" applyOnUpdate="0" field="Name"/>
    <default expression="" applyOnUpdate="0" field="Date"/>
    <default expression="" applyOnUpdate="0" field="Time"/>
    <default expression="" applyOnUpdate="0" field="Lon"/>
    <default expression="" applyOnUpdate="0" field="Lat"/>
    <default expression="" applyOnUpdate="0" field="Altitude"/>
    <default expression="" applyOnUpdate="0" field="North"/>
    <default expression="" applyOnUpdate="0" field="Azimuth"/>
    <default expression="" applyOnUpdate="0" field="Cam. Maker"/>
    <default expression="" applyOnUpdate="0" field="Cam. Model"/>
    <default expression="" applyOnUpdate="0" field="Title"/>
    <default expression="" applyOnUpdate="0" field="Comment"/>
    <default expression="" applyOnUpdate="0" field="Path"/>
    <default expression="" applyOnUpdate="0" field="RelPath"/>
    <default expression="" applyOnUpdate="0" field="Timestamp"/>
    <default expression="" applyOnUpdate="0" field="Images"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" notnull_strength="1" constraints="3" exp_strength="0" field="fid"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="ID"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Name"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Date"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Time"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Lon"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Lat"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Altitude"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="North"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Azimuth"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Cam. Maker"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Cam. Model"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Title"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Comment"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Path"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="RelPath"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Timestamp"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="Images"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="ID"/>
    <constraint exp="" desc="" field="Name"/>
    <constraint exp="" desc="" field="Date"/>
    <constraint exp="" desc="" field="Time"/>
    <constraint exp="" desc="" field="Lon"/>
    <constraint exp="" desc="" field="Lat"/>
    <constraint exp="" desc="" field="Altitude"/>
    <constraint exp="" desc="" field="North"/>
    <constraint exp="" desc="" field="Azimuth"/>
    <constraint exp="" desc="" field="Cam. Maker"/>
    <constraint exp="" desc="" field="Cam. Model"/>
    <constraint exp="" desc="" field="Title"/>
    <constraint exp="" desc="" field="Comment"/>
    <constraint exp="" desc="" field="Path"/>
    <constraint exp="" desc="" field="RelPath"/>
    <constraint exp="" desc="" field="Timestamp"/>
    <constraint exp="" desc="" field="Images"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column hidden="0" width="-1" name="fid" type="field"/>
      <column hidden="0" width="-1" name="ID" type="field"/>
      <column hidden="0" width="-1" name="Name" type="field"/>
      <column hidden="0" width="-1" name="Date" type="field"/>
      <column hidden="0" width="-1" name="Time" type="field"/>
      <column hidden="0" width="-1" name="Lon" type="field"/>
      <column hidden="0" width="-1" name="Lat" type="field"/>
      <column hidden="0" width="-1" name="Altitude" type="field"/>
      <column hidden="0" width="-1" name="North" type="field"/>
      <column hidden="0" width="-1" name="Azimuth" type="field"/>
      <column hidden="0" width="-1" name="Cam. Maker" type="field"/>
      <column hidden="0" width="-1" name="Cam. Model" type="field"/>
      <column hidden="0" width="-1" name="Title" type="field"/>
      <column hidden="0" width="-1" name="Comment" type="field"/>
      <column hidden="0" width="-1" name="Path" type="field"/>
      <column hidden="0" width="-1" name="RelPath" type="field"/>
      <column hidden="0" width="-1" name="Timestamp" type="field"/>
      <column hidden="0" width="-1" name="Images" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="Altitude" editable="1"/>
    <field name="Azimuth" editable="1"/>
    <field name="Cam. Maker" editable="1"/>
    <field name="Cam. Model" editable="1"/>
    <field name="Comment" editable="1"/>
    <field name="Date" editable="1"/>
    <field name="ID" editable="1"/>
    <field name="Images" editable="1"/>
    <field name="Lat" editable="1"/>
    <field name="Lon" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="North" editable="1"/>
    <field name="Path" editable="1"/>
    <field name="RelPath" editable="1"/>
    <field name="Time" editable="1"/>
    <field name="Timestamp" editable="1"/>
    <field name="Title" editable="1"/>
    <field name="fid" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Altitude"/>
    <field labelOnTop="0" name="Azimuth"/>
    <field labelOnTop="0" name="Cam. Maker"/>
    <field labelOnTop="0" name="Cam. Model"/>
    <field labelOnTop="0" name="Comment"/>
    <field labelOnTop="0" name="Date"/>
    <field labelOnTop="0" name="ID"/>
    <field labelOnTop="0" name="Images"/>
    <field labelOnTop="0" name="Lat"/>
    <field labelOnTop="0" name="Lon"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="North"/>
    <field labelOnTop="0" name="Path"/>
    <field labelOnTop="0" name="RelPath"/>
    <field labelOnTop="0" name="Time"/>
    <field labelOnTop="0" name="Timestamp"/>
    <field labelOnTop="0" name="Title"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"Name"</previewExpression>
  <mapTip>&lt;img src="file:///[% Path %]" width="350" height="250"></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
